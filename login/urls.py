from django.conf.urls import url

from login import views

urlpatterns = [
  url(r'^$', 'django.contrib.auth.views.login'),
  ]