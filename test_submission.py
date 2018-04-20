#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test a submitted Docker image.

Requires docker-keys.json to be set up.
Requires a submitted image.
Requires the openai/retro-env Docker image as explained in https://contest.openai.com/details

> docker pull openai/retro-env
> docker tag openai/retro-env remote-env
"""
import argparse
import codecs
import json
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Test a submitted Docker image locally.'
    )
    parser.add_argument('tag', type=str, help='the submission\'s tag')

    args = parser.parse_args()
    docker = {}

    with codecs.open('docker-keys.json', encoding='utf-8') as f:
        docker = json.load(f)

    url = docker['docker_registry_url']

    os.system(
        'retro-contest run --agent %s/%s '
        '--results-dir results --no-nv '
        '--use-host-data SonicTheHedgehog-Genesis GreenHillZone.Act1' %
        (url, args.tag)
    )
