# -*- coding: utf-8 *-*
from django.contrib import admin
from apps.requerimiento.models import Requirement, Project, Profile, ProfilesUser


class reqAdmin(admin.ModelAdmin):
    list_display = ('author', 'description', 'date_created',)
    search_fields = ('author__username', 'description', 'date_posted',)


class profileAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


class profileUserAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'profile',)


admin.site.register(Requirement, reqAdmin)
admin.site.register(Project,)
admin.site.register(Profile, profileAdmin)
admin.site.register(ProfilesUser, profileUserAdmin)
