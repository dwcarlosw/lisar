#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Terence Hong
terryhong@gmail.com

Django settings for LISAR project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


import os

SITE_ID = 1

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's$=_sc8mspe_(+vmg4fn*a@k+b77l25409m%rg(y&#_smlz!ht'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.comments',
    'rest_framework',
    # 'dh5bp',
    'bobthings',
    'translate',
    'rosetta',
    # 'tagging',
    # 'mptt',
)

# For blog.
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  # 'django.core.context_processors.i18n',
  'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # To let each individual user specify which language he or she prefer,
    # It should come after SessionMiddleware, And it should come before CommonMiddleware
    # If you use CacheMiddleware, put LocaleMiddleware after it.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

# LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_ROOT = "D:/HomeRepositories/Projects/LISAR/static/"

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    BASE_DIR+"/static",
    BASE_DIR+"/bobthings/static/js",
    BASE_DIR+"/bobthings/static/css",
)

LOCALE_PATHS = (
    BASE_DIR+'/translate/locale',
    BASE_DIR+'/bobthings/locale',
)



# Rosetta setts

ROSETTA_MESSAGES_PER_PAGE = 10