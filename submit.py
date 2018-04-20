#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Submit script"""
import argparse
import codecs
import json
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Submit a script to OpenAI')
    parser.add_argument('tag', type=str, help='the tag for the submission')

    args = parser.parse_args()
    docker = {}

    with codecs.open('docker-keys.json', encoding='utf-8') as f:
        docker = json.load(f)

    url = docker['docker_registry_url']
    username = docker['docker_registry_username']
    password = docker['docker_registry_password']

    os.system(
        'docker login %s --username "%s" --password "%s"' %
        (url, username, password))

    os.system('docker build -t %s/%s .' % (url, args.tag))

    os.system('docker push %s/%s' % (url, args.tag))
