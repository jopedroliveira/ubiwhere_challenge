from .base import *

SECRET_KEY = '@5CGHn&rxvsJwQPv3P?c9q7h#Vnx6FNbW&$VvU*@r7Sdf9?Bt7TjQ^$3WhcM_DC2H7'
DEBUG = True
LOCAL = True
HOST = 'http://localhost:8000'
ALLOWED_HOSTS = ['*']

POSTGRES_DB_DEFAULT_USER = 'montraficdbuser'
POSTGRES_DB_DEFAULT_PASSWORD = 'montraficdbpassword'
POSTGRES_DB_DEFAULT_PORT = '5432'
POSTGRES_DB_DEFAULT_NAME = 'montraficdb_dev'
POSTGRES_DB_DEFAULT_HOST = 'localhost'

DATABASES = {
  'default': {
    'ENGINE': "django.contrib.gis.db.backends.postgis",
    'NAME': POSTGRES_DB_DEFAULT_NAME,
    'USER': POSTGRES_DB_DEFAULT_USER,
    'PASSWORD': POSTGRES_DB_DEFAULT_PASSWORD,
    'HOST': POSTGRES_DB_DEFAULT_HOST,
    'PORT': POSTGRES_DB_DEFAULT_PORT,
  }
}

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=15),
  'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=10)
}
