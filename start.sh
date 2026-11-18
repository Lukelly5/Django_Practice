#!/bin/bash

# Run migrations
python manage.py migrate

# Start gunicorn
gunicorn learnin_log.wsgi:application