#!/usr/bin/python3
""" Just as in task #0, we’d like you to automate the task:
    of creating a custom HTTP header response,
    but with Puppet.
"""

from fabric.api import *
from os.path import exists


env.hosts = ["52.87.233.163", "100.27.0.20"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy archive! """
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except:
        return False
