#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
   that creates and distributes an archive to your web servers, using deploy.
"""
from datetime import datetime
from fabric.api import local, env, put, run
from fabric.utils import puts
import os


env.hosts = ['34.227.91.195', '52.86.130.233']
env.user = "ubuntu"


def deploy():
    """Creates and distributes an archive to your web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)


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


def do_deploy(archive_path):
    """Function that deploys an archive to my web servers"""

    if not os.path.exists(archive_path):
        return False

    try:
        # remove versions from archive_path
        archive_without_versions = archive_path.split('/')[1]

        # remove the file extension from archive_path
        archive_without_extension = archive_without_versions.split('.')[0]

        # path variables
        releases_path = "/data/web_static/releases/{}/"
        .format(archive_without_extension)
        tmp_path = "/tmp/{}".format(archive_without_versions)

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
