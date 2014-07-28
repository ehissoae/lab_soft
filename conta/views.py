from django.shortcuts import redirect
from django.conf import settings
from SiGeCAV.utils import *

def custom_login(request):
	url = url_if_not_authenticated(request)
	if(url):
		return url
		
	return redirect(settings.LOGIN_REDIRECT_URL)

# Create your views here.
