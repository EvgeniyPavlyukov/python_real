import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-x*$g0pktoj4js8_x9@!5^y*)'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '89.22.231.228']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2'
        'NAME': 'movie',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')