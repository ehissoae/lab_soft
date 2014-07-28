from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SiGeCAV.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # LOGIN
    url(r'', include('login.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recursos/', include('recursos.urls')),
    url(r'^acidentes/', include('acidentes.urls')),
    url(r'^acidentes/missoes/', include('missoes.urls')),
)
