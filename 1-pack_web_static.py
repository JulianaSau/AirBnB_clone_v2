#!/usr/bin/python3
"""This module defines a script that generates a .tgz archive from the contents of the web_static 
folder this repo,using the function do_pack
    Prototype: def do_pack():
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
    The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path if the archive has been correctly generated. 
    Otherwise, it should return None

"""

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date)
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception:
        return None