from django.urls import path

from . import views

app_name = 'mizukis_cafe'
urlpatterns = [
  path('', views.index, name='index'),
  path('add_beans', views.add_beans, name='add_beans'),
  path('modify_db', views.modify_db, name='modify_db'),
]