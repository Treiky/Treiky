# -*- coding: utf-8 *-*
from django.forms import ModelForm, Textarea, Select, TextInput
from apps.requerimiento.models import Requirement, Project
from django.contrib.auth.models import User


class reqForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(reqForm, self).__init__(*args, **kwargs)
        self.fields['project'].label = "Para el proyecto"
        self.fields['role'].label = "Yo como"
        self.fields['priority'].label = "Esto importa"
        self.fields['description'].label = "Quiero poder"
        self.fields['project'].error_messages={'required': 'Debe seleccionar un proyecto'}
        self.fields['role'].error_messages={'required': 'El campo es requerido'}
        self.fields['description'].error_messages={'required': 'El campo es requerido'}

    class Meta:
        model = Requirement
        widgets = {
            'project': Select(),
            'role': TextInput,
            'priority': Select(),
            'description': Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        fields = ('project', 'role', 'description', 'priority')
        exclude = ['author', 'date_created']


class projForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(projForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nombre del Proyecto"
        self.fields['description'].label = "Descripcion"
        self.fields['name'].error_messages = {'required': 'El nombre es requerido'}
        self.fields['description'].error_messages = {'required': 'La descripcion es requerida'}

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
        self.fields['username'].error_messages={'required': 'El nombre de usuario es requerido'}
        self.fields['last_name'].error_messages={'required': 'La nombre es requerida'}
        self.fields['last_name'].error_messages={'required': 'El apellido es requerido'}
        self.fields['email'].error_messages={'required': 'El Email es requerido'}


    class Meta:
        model = User
        widgets = {
            'username': TextInput,
            'first_name': TextInput,
            'last_name': TextInput,
            'email': TextInput,
        }
        fields = ('username', 'first_name', 'last_name', 'email')

