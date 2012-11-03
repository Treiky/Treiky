# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.requerimiento.models import Requirement, Project, ProfilesUser
from apps.requerimiento.forms import reqForm, projForm, projectSearchV2, asigUserProj, editUserForm


@login_required
def view_req(request):
    a = ProfilesUser.objects.filter(user=request.user).only('project')
    b = [x.project.id for x in a]
    print b
    return render_to_response(
        'list_Requirements.html',
        RequestContext(
            request,
            {'requerimiento': Requirement.objects.filter(project__id__in = b).order_by('-date_created'),}
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
        form = reqForm(initial=request.user)
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Publique su nuevo Requerimiento:',
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

    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de Proyectos:',
        }))




def resultado_alta_usuario(request):
    return render_to_response('respuesta.html', RequestContext(request, {
        'mensaje': 'El alta se registro correctamente, recibira la clave por email ',
        }))


def resultado_alta_proyecto(request):
    return render_to_response('respuesta.html', RequestContext(request, {
        'mensaje': 'El cambio se realizo con exito',
        }))


def logoutuser(request):
    logout(request)
    return render_to_response('index.html', RequestContext(request, {
        'mensaje': 'El proyecto se dio del alta correctamente',
        }))


@login_required
def update_project(request):
    layout = 'vertical'
    idproject = 0

    if request.method == 'POST':
        form = projForm(request.POST)
        idproject = request.POST.get('idproject', '')
        if form.is_valid():
            new_proj = form.save(commit=False)
            new_proj.id = request.session['idProject']
            new_proj.name
            new_proj.description
            new_proj.save(force_update=True)
            return resultado_alta_proyecto(request)
    else:
        b = ProfilesUser.objects.filter(project__name=request.session['Proyecto'], user=request.user, profile__id=1)
        a = []
        for Perfuser in b:
            a = Project.objects.filter(name=request.session['Proyecto'], user=Perfuser.user)
        form = projForm()
        for proj in a:
            idproject = proj.id
            form = projForm(initial={
                'name': proj.name,
                'description': proj.description
                })

    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'id': idproject,
        'title': 'Modificacion de Projecto:',
        }))


@login_required
def searchProject(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = projectSearchV2(request.POST)
        a = request.POST.get('project', '')
        print a
        request.session['idProject'] = a
        projectNombre = Project.objects.filter(id=a).only('name')
        request.session['Proyecto'] = projectNombre[0]
        request.method = ''
        return HttpResponseRedirect("/update_project/")
    else:
        form = projectSearchV2(initial=request.user)
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Editor de Proyecto',
        }))



@login_required
def asig_user(request):
    layout = 'vertical'

    if request.method == 'POST':
        form = asigUserProj(request.POST)
        if form.is_valid:
            new_req = form.save(commit=False)
            new_req.save()
            return resultado_alta_proyecto(request)
    else:
        form = asigUserProj(initial=request.user)
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Publique su nuevo Requerimiento:',
        }))


def new_user(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = UserCreationForm()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Alta de usuario:',
        }))


def edit_user(request):
    layout = 'vertical'
    if request.method == 'POST':
        form = editUserForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
    else:
        form = editUserForm(instance=request.user)
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
        'layout': layout,
        'title': 'Editar de usuario:',
        }))

