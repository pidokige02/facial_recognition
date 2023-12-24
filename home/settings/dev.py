'''Use this for development'''
from .base import *

ALLOWED_HOSTS += ['127.0.0.1',
                  '13.124.235.245',
                  'face.hobbycoding.site'  
                  ]

DEBUG = True

WSGI_APPLICATION = 'home.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)

STRIPE_PUBLISH_KEY = ''
# STRIPE_SECRET_KEY = 'sk_test_51Mgb8FDVRmxkeQOrSoPpPJQhdPRbm0CRsRoNEuJ85CG6Hfr3h8IvtkprAJZPCs8DxvBfidZ3moFSQSniFv7CSqL900ZjW7xbVp'
STRIPE_PUBLISH_KEY = 'pk_test_TYooMQauvdEDq54NiTphI7jx'
STRIPE_SECRET_KEY = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'