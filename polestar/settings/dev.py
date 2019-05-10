from .base import *

DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b_hqce*z2anyu*s3m4%5oox)r4_rt5vk0m+dxxopw71rt!g2x9'

ALLOWED_HOSTS = []

CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('SQL_DATABASE', 'postgres'),
        'USER': os.getenv('SQL_USER', 'postgres'),
        'PASSWORD': os.getenv('SQL_PASSWORD', ''),
        'HOST': os.getenv('SQL_HOST', 'db'),
        'PORT': os.getenv('SQL_PORT', '5432'),
    }
}