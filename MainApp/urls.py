from django.urls import path

from . import views

appname = 'MainApp'

urlpatterns = [
    path('', views.index, name='index'),
    