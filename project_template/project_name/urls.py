# -*- coding: utf-8 -*-
# Admin activé par défaut
from {{project_name}} import settings

from django.contrib import admin
from django.conf.urls import patterns, include, url

# Comment the next line to disable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Comment the next two lines to disable admin & admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # url(r'^app/', include('apps.app.urls', namespace='app')),
)

# Servir les médias statiques en développement + activer les index
# Cf: https://docs.djangoproject.com/en/1.2/howto/static-files/#limiting-use-to-debug-true
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
