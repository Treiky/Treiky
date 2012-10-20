# -*- coding: utf-8 *-*
from django.forms import ModelForm, Textarea, Select, TextInput
from django import forms
from apps.requerimiento.models import Requirement, Project, ProfilesUser
from django.contrib.auth.models import User

PRIORIDAD_CHOICES = (
    ('Poco', 'Poco'),
    ('Medio', 'Medio'),
    ('Mucho', 'Mucho'),)


class reqForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user_details = kwargs.pop('initial', None)
        super(reqForm, self).__init__(*args, **kwargs)
        self.fields['project'].label = "Para el proyecto"
        self.fields['role'].label = "Yo como"
        self.fields['priority'].label = "Esto importa"
        self.fields['description'].label = "Quiero poder"
        self.fields['project'].error_messages = {
            'required': 'Debe seleccionar un proyecto'}
        self.fields['role'].error_messages = {
            'required': 'El campo es requerido'}
        self.fields['description'].error_messages = {
            'required': 'El campo es requerido'}
        self.fields['project'].queryset = Project.objects.filter(
            user=user_details)

    class Meta:
        model = Requirement
        widgets = {
            'project': Select(),
            'role': TextInput(),
            'priority': Select(choices=PRIORIDAD_CHOICES),
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        fields = ('project', 'role', 'description', 'priority')
        exclude = ['author', 'date_created']


class projForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(projForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nombre del Proyecto"
        self.fields['description'].label = "Descripcion"
        self.fields['name'].error_messages = {
            'required': 'El nombre es requerido'}
        self.fields['description'].error_messages = {
            'required': 'La descripcion es requerida'}

    class Meta:
        model = Project
        widgets = {
            'name': TextInput,
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        fields = ('name', 'description')


class newUserForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(newUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"
        self.fields['username'].error_messages = {
            'required': 'El nombre de usuario es requerido'}
        self.fields['last_name'].error_messages = {
            'required': 'La nombre es requerida'}
        self.fields['last_name'].error_messages = {
            'required': 'El apellido es requerido'}
        self.fields['email'].error_messages = {
            'required': 'El Email es requerido'}

    class Meta:
        model = User
        widgets = {
            'username': TextInput,
            'first_name': TextInput,
            'last_name': TextInput,
            'email': TextInput,
        }
        fields = ('username', 'first_name', 'last_name', 'email')


class asigUserProj(ModelForm):

    def __init__(self, *args, **kwargs):
        user_details = kwargs.pop('initial', None)
        super(asigUserProj, self).__init__(*args, **kwargs)
        self.fields['project'].label = "Para el proyecto"
        self.fields['user'].label = "Usuario"
        self.fields['profile'].label = "Perfil"
        self.fields['project'].error_messages = {
            'required': 'Debe seleccionar un proyecto'}
        self.fields['user'].error_messages = {
            'required': 'Debe seleccionar un usuario'}
        self.fields['profile'].error_messages = {
            'required': 'Debe seleccionar un perfil'}
        self.fields['project'].queryset = Project.objects.filter(
            user=user_details)

    class Meta:
        model = ProfilesUser
        widgets = {
            'project': Select(),
            'user': Select(),
            'profile': Select(),
        }
        fields = ('project', 'user', 'profile')


class RegistroUsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class projectSearch(forms.Form):
    project = forms.CharField(label = "Ingrese el nombre del proyecto a editar")
