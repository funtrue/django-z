#!/bin/bash

# start shell
mkdir -p log
nohup gunicorn django_z.wsgi -c django_z/gunicorn_config.py >> /dev/null 2>&1 &
nohup python3 manage.py qcluster >> /dev/null 2>&1