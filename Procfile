web: gunicorn HextomTakeHome.wsgi --log-file -
worker: celery -A HextomTakeHome worker -l --max-tasks-per-child 10 info
beat: celery -A HextomTakeHome beat -l info