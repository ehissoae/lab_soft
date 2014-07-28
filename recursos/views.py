from django.shortcuts import render
from recursos.models import Recurso

# Create your views here.
def index(request):
  recursos = Recurso.objects.all()
  return render(request, 'recursos/index.html', {'recursos': recursos})