from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views

admin.autodiscover()

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^conta/', include('conta.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recursos/', include('recursos.urls')),
    url(r'^acidentes/missoes/', include('missoes.urls')),
    url(r'^acidentes/', include('acidentes.urls')),
    url(r'^', include('home.urls')),
)
