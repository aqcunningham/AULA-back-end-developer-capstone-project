<!-- web: gunicorn myproject.wsgi --log-file - -->
web: python manage.py collectstatic --noinput && gunicorn myproject.wsgi --log-file -
