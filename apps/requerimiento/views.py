# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.requerimiento.models import Requirement
from apps.requerimiento.forms import reqForm, projForm, newUserForm

@login_required
def view_req(request):
    return render_to_response(
        'list_Requirements.html',
        RequestContext(
            request,
            {'requerimiento': Requirement.objects.order_by('-date_created')}
            ),
                )


@login_required
def write_req(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = reqForm(request.POST)
        if form.is_valid():
            new_req = form.save(commit=False)
            new_req.author = request.user
            new_req.save()
            return view_req(request)
    else:
        form = reqForm()

    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        }))


@login_required
def write_project(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = projForm(request.POST)
        if form.is_valid():
            new_proj = form.save(commit=False)
            new_proj.save()
            return resultado_alta_proyecto(request)
    else:
        form = projForm()

    return render_to_response('form_Proyectos.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        }))


def new_user(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = newUserForm(request.POST)
        if form.is_valid():
            new_proj = form.save(commit=False)
            new_proj.save()
            return resultado_alta_usuario(request)
    else:
        form = newUserForm()

    return render_to_response('registration/alta.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        }))

def resultado_alta_usuario(request):
    layout = 'vertical'

    return render_to_response('respuesta.html', RequestContext(request, {
        'mensaje': 'El alta se registro correctamente, recibira la clave por email',
        }))

def resultado_alta_proyecto(request):
    layout = 'vertical'
    return render_to_response('respuesta.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))


def logoutuser(request):
    logout(request)
    return render_to_response('index.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))
