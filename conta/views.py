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

    num_users_with_same_email = User.objects.filter(email=email).count()
    num_users_with_same_username =  User.objects.filter(username=username).count()

    if num_users_with_same_email != 0 and num_users_with_same_username != 0:
      messages.error(request, 'Usuário e E-mail já existem.')
    elif num_users_with_same_username != 0:
      messages.error(request, 'Usuário já existe.')
    elif num_users_with_same_email != 0:
      messages.error(request, 'Usuário com o mesmo e-mail já existe.')
    else:
      if first_name and email and username and password and tipoAcesso:
        user = User.objects.create(first_name=first_name, email=email, username=username, password=password)
        profile = Profile.objects.create(tipoAcesso=tipoAcesso, user=user)
        return redirect(profile)
    return render(request, 'registration/novo.html', {
      'first_name': first_name,
      'email': email,
      'username': username,
      'password': password,
      'tipoAcesso': tipoAcesso,
      'role_choices': Profile.ROLE_CHOICES,
      })

def edit(request):
  if request.method == "GET":
    userId = request.GET.get("id", "")
    user = User.objects.get(id=userId)
    return render(request, 'registration/editar.html', {'usuario': user, 'role_choices': Profile.ROLE_CHOICES})
  elif request.method == "POST":
    userId = request.POST.get("id", "")
    user = User.objects.get(id=userId)

    user.first_name = request.POST.get("firstName", "")
    user.email = request.POST.get("email", "")
    user.username = request.POST.get("username", "")

    tipoAcesso = request.POST.get("tipoAcesso", "")
    if Profile.objects.filter(id=user.id).count():
      user.profile.tipoAcesso = tipoAcesso
    else:
      Profile.objects.create(user=user, tipoAcesso=tipoAcesso)

    newPassword = request.POST.get("newPassword", "")
    if newPassword:
      user.set_password(newPassword)

    user.save()
    user.profile.save()
    return redirect(user.profile)

def delete(request):
  usuarioId = request.GET.get("id", "")
  User.objects.get(id=usuarioId).delete()
  return redirect('usuarios')
