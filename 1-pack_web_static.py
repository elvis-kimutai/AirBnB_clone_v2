#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric import task
from invoke import run
from os.path import isdir

@task
def do_pack(c):
    """Generates a .tgz archive from web_static"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            run("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        run("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    pass
