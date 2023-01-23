#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """generates a tgz archive"""
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        time = datetime.now()
        fmt = "%Y%m%d%H%M%S"
        file_path = 'versions/web_static_{}.tgz'.format(time.strftime(fmt))
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path
    except ValueError:
        return None
