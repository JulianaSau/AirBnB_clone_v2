#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
   that creates and distributes an archive to your web servers, using the function deploy.
"""
from fabric.api import env
from os.path import exists

# Importing functions from separate modules
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ['34.227.91.195', '52.86.130.233']
env.user = "ubuntu"


def deploy():
    """Creates and distributes an archive to your web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

