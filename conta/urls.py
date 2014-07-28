from django.conf.urls import url

from conta import views

urlpatterns = [
  url(r'^login$', views.custom_login, name="custom_login"),
  url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/conta/login'}),
  ]