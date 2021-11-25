web: gunicorn HextomTakeHome.wsgi --log-file -
worker: celery -A --max-tasks-per-child 10 HextomTakeHome worker -l info
beat: celery -A HextomTakeHome beat -l info