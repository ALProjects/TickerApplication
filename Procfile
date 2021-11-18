web: gunicorn HextomTakeHome.wsgi --log-file -
worker: celery -A HextomTakeHome worker -l info
beat: celery -A HextomTakeHome beat -l info