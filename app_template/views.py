# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.utils.translation import ugettext_lazy as _

def my_view(request):
    """Retourne l'index de l'application"""
    
    return render(request, {}, '{{ app_name }}/index.html')
