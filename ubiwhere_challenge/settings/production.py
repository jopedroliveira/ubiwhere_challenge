from .base import *

SECRET_KEY = 'rxwmG5WfSRZD#bCW$jak2b4h5-6993W+DxN&2J?Yx7WFf*es23@+6DVggcp3B_yjtg'
DEBUG = False
LOCAL = True
HOST = 'http://localhost'
ALLOWED_HOSTS = ['*']

POSTGRES_DB_DEFAULT_USER = 'montraficdbuser'
POSTGRES_DB_DEFAULT_PASSWORD = 'montraficdbpassword'
POSTGRES_DB_DEFAULT_PORT = '5432'
POSTGRES_DB_DEFAULT_NAME = 'montraficdb'
POSTGRES_DB_DEFAULT_HOST = 'database_montraficdb'

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
