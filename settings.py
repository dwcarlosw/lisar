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

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


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

    # third party library
    'rest_framework',
    'south',
    'mptt',
    'django_mptt_admin',
    'modeltranslation',
    'rosetta',
    'reversion',
    'reversion_compare',
    'xadmin',
    'crispy_forms',
    'taggit',
    'filer',
    # 'dh5bp',


    'bobthings',
    'project_lisar',
    'ticketing',
    '_misc',
    'translate',

    # 'tagging',
    # 'cms',

    # 'bootstrap3',
    # 'menus',
    # 'south',
    # 'sekizai',
)

# For blog.
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  # 'django.core.context_processors.i18n',
  "django.core.context_processors.static",
  'django.core.context_processors.request',
  # "account.context_processors.account", # used by django-user-accounts
)

TEMPLATE_DIRS = (
	# The docs say it should be absolute path: PROJECT_PATH is precisely one.
	os.path.join(BASE_DIR, "project_lisar/templates"),
    os.path.join(BASE_DIR, "ticketing/templates"),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # To let each individual user specify which language he or she prefer,
    # It should come after SessionMiddleware, And it should come before CommonMiddleware
    # If you use CacheMiddleware, put LocaleMiddleware after it.
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'reversion.middleware.RevisionMiddleware',

    #require users to log in to access site
    'project_lisar.middleware.EnforceLoginMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lisar',
        'USER': os.environ['LOCAL_DB_USER'],
        'PASSWORD': os.environ['LOCAL_DB_PASS'],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#model translation
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('zh-cn', gettext('Chinese Simplified')),
)
MODELTRANSLATION_DEFAULT_LANGUAGE = ('en')

MODELTRANSLATION_TRANSLATION_FILES = (
    'bobthings.translation',
    'ticketing.translation'
)

# MODELTRANSLATION_CUSTOM_FIELDS = ('MyField', 'MyOtherField',)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_ROOT = "D:/HomeRepositories/Projects/LISAR/static/"

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    BASE_DIR+"/project_lisar/static",
    BASE_DIR+"/project_lisar/static/css",
    BASE_DIR+"/project_lisar/static/js",
    BASE_DIR+"/project_lisar/static/images",

    BASE_DIR+"/bobthings/static/js",
    BASE_DIR+"/bobthings/static/css",

    BASE_DIR+"/ticketing/static/css",
)

LOCALE_PATHS = (
    BASE_DIR+'/project_lisar/locale',
    BASE_DIR+'/translate/locale',
    BASE_DIR+'/bobthings/locale',
)

FIXTURE_DIRS = (
   BASE_DIR+'/bobthings/fixtures/',
)

# Rosetta settings

ROSETTA_MESSAGES_PER_PAGE = 10
ROSETTA_REQUIRES_AUTH = True
LOGIN_URL = '/api-auth/login/' # page for logging into rosetta
LOGOUT_URL = '/admin/logout/'