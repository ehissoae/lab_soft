from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.conf import settings
from SiGeCAV.utils import *

def custom_login(request):
	redirect = url_if_not_authenticated(request)
	if(redirect):
		return redirect
		
	return redirect(settings.LOGIN_REDIRECT_URL)

# Create your views here.
