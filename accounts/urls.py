from django.conf.urls import url

from accounts import views

urlpatterns = [
  url(r'^login$', 'django.contrib.auth.views.login'),
  url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}),
  ]