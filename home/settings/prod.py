from .base import *

DEBUG = False
ALLOWED_HOSTS += ['127.0.0.1',
                  '13.124.235.245',
                  'face.hobbycoding.site'
                  ]

WSGI_APPLICATION = 'home.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'dbuser',
        'PASSWORD': 'donkey123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STRIPE_PUBLISH_KEY = 'pk_test_TYooMQauvdEDq54NiTphI7jx'
STRIPE_SECRET_KEY = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

CORS_ORIGIN_ALLOW_ALL = True