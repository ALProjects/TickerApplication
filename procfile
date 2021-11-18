web: gunicorn locallibrary.wsgi --log-file -
worker: celery worker --app=tasks.app