#!/usr/bin/python3
"""This module defines a script that generates a .tgz archive from the contents of the web_static
    folder this repo,using the function do_pack"""

from datetime import datetime
from fabric.api import local
from fabric.utils import puts
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not os.path.exists("versions"):
            local('mkdir -p versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(date)
        puts("Packing web_static to {}".format(archive_path))

        if local('tar -cvzf {} web_static'.format(archive_path)).succeeded:
            puts("web_static packed: {}".format(archive_path))
            return archive_path
    except Exception:
        return None
