# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

## Simple registration :
# admin.site.register(ExampleModel)
#
## Complète :
# class ExampleModelAdmin(admin.ModelAdmin):    
#     ## Affichage en liste
#     list_display = ('',) # affichage en liste
#     list_editable = ('',) # champ que l'on peut modifier dans la liste
#     date_hierarchy = '' # tri par date
#     list_filter = ('sample', 'related_obj__attr_of_the_rel_obj',)
#     
#     list_max_show_all = 200
#     list_per_page = 100
#     
#     # autres méthodes à appliquer à la sélection par liste
#     actions = ['false_bool']
#     
#     def false_bool(self, request, queryset):
#         queryset.update(bool_attr=False)
#     false_bool.short_description = "Bool > False"
#     
#     ## Affichage en édition/création
#     fields = ('',) # ce qu'on peut modifier ou bien :
#     
#     # gère l'affichage des fichiers
#     fieldsets = (
#         (None, {
#             'fields': (('name', 'slug'), 'other')
#         }),
#         ('Advanced options', {
#             'classes': ('collapse', 'wide'), # collapse cache, wide étend
#             'fields': ('text_field')
#         }),
#     )
#     
#     readonly_fields = ('',) # empêche l'édition mais pas l'affichage
#     
#     form = ExampleModelForm # utilise un formulaire perso
#     
#     prepopulated_fields = {"slug": ("name",)}
#     
#     # remplace la liste déroulante d'un ForeignKey ou d'un choices
#     # par des boutons radio
#     radio_fields = {"sample": admin.VERTICAL}
#     
#     # Éditer un modèle à l'intérieur (ForeignKey)
#     inlines = [ExampleRelInline,]
#     
# class ExampleRelInline(admin.TabularInline):
#     model = ExampleRelation
# 
# admin.site.register(ExampleModel, ExampleModelAdmin)
