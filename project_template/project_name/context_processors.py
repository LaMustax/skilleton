# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site

def current_site(request):
    """Ajoute le site courant via current_site"""
    try:
        current_site = Site.objects.get_current()
        return {
            'current_site': current_site,
        }
    except Site.DoesNotExist:
        # il faut bien retourner quelque chose :
        return {'current_site':''}
