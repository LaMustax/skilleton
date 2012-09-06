#!/usr/bin/python
# -*- coding: utf-8 -*-
# Cf: http://wiki.alwaysdata.com/wiki/D%C3%A9ployer_une_application_Django
#
# Décommenter les 4 lignes suivantes pour activer le virtualenv 
#  (en supposant qu'il soit dans le dossier $HOME/.virtualenvs) :
# import getpass
# 
# venv = '/home/{0}/.virtualenvs/{1}/bin/activate_this.py'.format(getpass.getuser(), NOM_DU_VIRTUALENV)
# execfile(venv, dict(__file__=venv))

import sys
from os import environ
from os.path import abspath, basename, dirname
from django.core.servers.fastcgi import runfastcgi

_PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, _PROJECT_DIR)
sys.path.insert(0, dirname(_PROJECT_DIR))

_PROJECT_NAME = basename(_PROJECT_DIR)
environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

runfastcgi(method="threaded", daemonize="false")
