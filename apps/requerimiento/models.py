# -*- coding: utf-8 -*-
from django.db import models

import datetime
from django.contrib.auth.models import User


class Project(models.Model):

    name = models.TextField(max_length=20)
    description = models.TextField(max_length=150)
    user = models.ManyToManyField(User, blank=True, null=True)

    def __unicode__(self):
        return "%s" % (self.name,)


class Profile(models.Model):
    #Recorda que siempre el Primero debe ser el admin
    #El segundo el Colaborador
    #y el tercero el usuario comun
    name = models.TextField(max_length=20)
    description = models.TextField(max_length=50)

    def __unicode__(self):
        return "%s" % (self.name,)


class ProfilesUser(models.Model):

    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)

    def __unicode__(self):
        return "Project: %s User: %s" % (self.project, self.user)


class Requirement(models.Model):
    """
    Model to represent the requerimiento.
    """
    author = models.ForeignKey(User, blank=True, null=True)
    project = models.ForeignKey(Project)
    role = models.TextField(max_length=10)
    priority = models.TextField(max_length=8)
    description = models.TextField(max_length=140)
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "Author: %s, Requirement: %s" % (
            self.author.username, self.description,)

