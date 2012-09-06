# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

# CHOICES = (('A', 'Sample'),)
# 
# class ExampleModel(models.Model):
#     name = models.CharField(_('Nom'), max_length=255, default='A', choices=CHOICES, help_text=_('Concis, Précis'))
#     slug = models.SlugField(max_length=255, null=True, blank=True, editable=False, unique=True)
#     
#     class Meta:
#         ordering = ['-date_example_field', 'name']
#         get_latest_by = 'date_example_field'
#         verbose_name = _('Exemple')
#         verbose_plural_name = _('Exemples')
