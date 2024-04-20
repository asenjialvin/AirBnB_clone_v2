#!/usr/bin/python3
"""Fabric script to deploy archives to web servers
"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['100.26.133.136', '54.221.184.20']
env.user = 'ubuntu'
env.key_filename = '~/keys/aprkey'

def do_deploy(archive_path):
    """Distribute archive to web servers
    """
    try:
        if not path.exists(archive_path):
            return False

        # Upload archive
        put(archive_path, '/tmp/')

        # Extract archive and delete .tgz
        filename = archive_path.split('/')[-1]
        foldername = filename.split('.')[0]
        release_path = '/data/web_static/releases/' + foldername

        run('sudo mkdir -p {}'.format(release_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(filename, release_path))
        run('sudo rm /tmp/{}'.format(filename))

        # Remove existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create new symbolic link
        run('sudo ln -s {} /data/web_static/current'.format(release_path))

        return True
    except:
        return False

