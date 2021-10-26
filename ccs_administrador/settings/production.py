from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cssadministrador.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'da0ijl1evhpak6',
        'USER': 'lnamsplssaupkx',
        'PASSWORD': 'cfa7ee88a800551c052991d2bf381679abfdc0c92fdc1ae92a0484d783afb6b4',
        'HOST': 'ec2-52-0-234-93.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}


STATICFILES_DIRS = (BASE_DIR, 'static')
