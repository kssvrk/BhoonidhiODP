#!/bin/bash
# Name of the application
NAME="django_starter"
# Django project directory
DJANGODIR=/home/radhakrishna/projects/django_starter/source
# we will communicte using this TCP PORT
PORT=9000
LOGFILE=/home/radhakrishna/projects/django_starter/logs/gunicorn.log
# the user to run as
USER=radhakrishna
# the group to run as
GROUP=radhakrishna
# how many worker processes should Gunicorn spawn
NUM_WORKERS=3
# which settings file should Django use
DJANGO_SETTINGS_MODULE=app.settings
# WSGI module name
DJANGO_WSGI_MODULE=app.wsgi

#---------------------------------------- MOSTLY NEED NOT TOUCH BELOW THIS -------------------------
echo "Starting $NAME as `whoami`"
# Activate the virtual environment
cd $DJANGODIR
# source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind 0.0.0.0:$PORT \
--log-level=debug \
--log-file=$LOGFILE