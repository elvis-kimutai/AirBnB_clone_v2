#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""
from fabric.api import put, run, env
from datetime import datetime
from os.path import exists

env.hosts = ['54.90.10.90', '3.85.177.221']
def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        # Extract necessary information from the archive filename
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload the archive to the remote server's /tmp/ directory
        put(archive_path, '/tmp/')

        # Create the release directory
        run('mkdir -p {}{}/'.format(path, no_ext))

        # Extract the contents of the archive to the release directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))

        # Clean up by removing the temporary archive
        run('rm /tmp/{}'.format(file_n))

        # Move the contents to the appropriate location
        run('mv {}{}/web_static/* {}{}/'.format(path, no_ext, path, no_ext))

        # Remove the web_static directory
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        # Remove the existing 'current' symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new 'current' symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
