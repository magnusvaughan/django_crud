# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'culture')

admin.site.register(Character, CharacterAdmin)