# -*- coding: utf-8 -*-
# Configuration lors du développement
# Cf: https://code.djangoproject.com/wiki/SplitSettings#SimplePackageOrganizationforEnvironments

from os.path import join, normpath

from defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': normpath(join(PROJECT_ROOT, '{{project_name}}','default.db')), # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# # #
# TEMPLATES
#
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

# # #
# APPS
# 
INSTALLED_APPS += (
    'debug_toolbar',
)

# # #
# CACHE
#
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# # #
# EMAILS
#
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# # #
# DEBUG TOOLBAR
#
INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
