#!/usr/bin/python3
"""This module describes a script (based on the file 1-pack_web_static.py)
    that distributes an archive to my web servers, using do_deploy:"""

from datetime import datetime
from fabric.api import local, env, put, run
import os


env.hosts = ['34.227.91.195', '52.86.130.233']
env.user = "ubuntu"


def do_deploy(archive_path):
    """Function that deploys an archive to my web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        # remove versions from archive_path
        archive_file = archive_path.split('/')[1]

        # remove the file extension from archive_path
        archive_name = archive_file.split('.')[0]

        # path variables
        releases_path = "/data/web_static/releases/{}/".format(archive_name)
        tmp_path = "/tmp/{}".format(archive_file)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Create releases directory if it doesn't exist
        run("mkdir -p {}".format(releases_path))

        # Uncompress the archive to the folder /data/web_static/releases/
        # <archive filename without extension> on the web server
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))

        # Delete the archive from the web server
        run("rm {}".format(tmp_path))

        # Move the content of the web_static folder to the new version folder
        run("mv {}web_static/* {}".format(releases_path, releases_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf {}web_static".format(releases_path))

        # Create a new symbolic link on the web server
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))

        print("New version deployed!")

        return True
    except Exception as e:
        return False
