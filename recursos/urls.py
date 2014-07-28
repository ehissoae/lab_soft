from django.conf.urls import url

from recursos import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]