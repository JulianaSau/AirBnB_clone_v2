#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
   that creates and distributes an archive to your web servers, using the function deploy.
"""
from datetime import datetime
from fabric.api import local, env, put, run
from fabric.utils import puts
import os


env.hosts = ['34.227.91.195', '52.86.130.233']
env.user = "ubuntu"


def do_clean(number=0):
    """Function that cleans up out-of-date archives
        Args:
        number - number of the archives, including the most recent, to keep
    """

    # if number is 0 or 1 keep only one release, else limit is number
    number = 1 if int(number) == 0 else int(number)

    # Local clean
    local("ls -t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))

    releases_path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(releases_path, number + 1))
