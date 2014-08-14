# -*- coding: utf-8 -*-

from django.shortcuts import redirect
from django.conf import settings
from SiGeCAV.utils import *
from django.contrib.auth.models import User
from conta.models import Profile
from django.contrib import messages 

def custom_login(request):
	url = url_if_not_authenticated(request)
	if(url):
		return url
		
	return redirect(settings.LOGIN_REDIRECT_URL)

def index(request):
  usuarios = User.objects.all()
  return render(request, 'registration/index.html', {'usuarios': usuarios})

def detail(request):
  usuarioId = request.GET.get("id", "")
  usuario = User.objects.get(id=usuarioId)
  return render(request, 'registration/detalhes.html', {'usuario': usuario})

def new(request):
  if request.method == "GET":
    return render(request, 'registration/novo.html', {'role_choices': Profile.ROLE_CHOICES})
  elif request.method == "POST":
    first_name = request.POST.get("firstName", "")
    email = request.POST.get("email", "")
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    tipoAcesso = request.POST.get("tipoAcesso", "")

    if first_name and email and username and password and tipoAcesso:
      num_users_with_same_email = User.objects.filter(email=email).count()
      num_users_with_same_username =  User.objects.filter(username=username).count()
      if num_users_with_same_email + num_users_with_same_username == 0:
        user = User.objects.create(first_name=first_name, email=email, username=username, password=password)
        profile = Profile.objects.create(tipoAcesso=tipoAcesso, user=user)
        return index(request)
      elif num_users_with_same_username != 0:
        messages.error(request, 'Usuário já existe.')
      elif num_users_with_same_email != 0:
        messages.error(request, 'Usuário com o mesmo e-mail já existe.')
      else:
        messages.error(request, 'Usuário e E-mail já existem.')
    return render(request, 'registration/novo.html', {})

def edit(request):
  if request.method == "GET":
    usuarioId = request.GET.get("id", "")
    usuario = User.objects.get(id=usuarioId)
    return render(request, 'registration/editar.html', {'usuario': usuario, 'role_choices': Profile.ROLE_CHOICES})
  elif request.method == "POST":
    usuarioId = request.POST.get("id", "")
    usuario = User.objects.get(id=usuarioId)

    usuario.first_name = request.POST.get("firstName", "")
    usuario.email = request.POST.get("email", "")
    usuario.username = request.POST.get("username", "")
    usuario.password = request.POST.get("password", "")
    usuario.save()
    return render(request, 'registration/detalhes.html', {'usuario': usuario})

def delete(request):
  usuarioId = request.GET.get("id", "")
  User.objects.get(id=usuarioId).delete()
  return index(request)