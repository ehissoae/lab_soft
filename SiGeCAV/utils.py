from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.conf import settings

def url_if_not_authenticated(request):
    if not request.user.is_authenticated():
        return login(request)
