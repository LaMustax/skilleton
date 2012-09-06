# -*- coding: utf-8 -*-
# Configuration lors de la mise en production
# Cf: https://code.djangoproject.com/wiki/SplitSettings#SimplePackageOrganizationforEnvironments
from defaults import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# # #
# EMAILS
#
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = "smtp.alwaysdata.com"
# EMAIL_HOST_PASSWORD = None
# EMAIL_HOST_USER = None
# EMAIL_PORT = None
# EMAIL_SUBJECT_PREFIX = None
# EMAIL_USE_TLS = True
