# -*- coding: utf-8 *-*
from django.contrib import admin
from apps.requerimiento.models import Requirement, Project


class reqAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'date_created',)
    search_fields = ('author__username', 'description', 'date_posted',)

admin.site.register(Requirement, reqAdmin)
admin.site.register(Project,)
