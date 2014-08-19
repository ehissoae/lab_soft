# -*- coding: utf-8 -*-

from django.shortcuts import render
from recursos.models import Recurso
from SiGeCAV.utils import *
from django.contrib import messages 

def relatorio(request):
  return render(request, 'relatorio.html', {})

def gerarRelatorio(request):
  return render(request, 'gerarRelatorio.html', {})