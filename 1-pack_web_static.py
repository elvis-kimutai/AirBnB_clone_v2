#!/usr/bin/python3
"""
Function to create a .tgz archive from web_static folder
"""
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """creates a tgz archive of web_ststic direcrory"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
