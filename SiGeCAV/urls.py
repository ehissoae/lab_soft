from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views

admin.autodiscover()

urlpatterns = patterns('django.contrib.auth.views',
    # Examples:
    # url(r'^$', 'SiGeCAV.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # LOGIN
    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recursos/', include('recursos.urls')),
    url(r'^home/', include('home.urls')),
)
