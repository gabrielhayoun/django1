from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.albums, name='albums'),
    path('<int:id>', views.track, name='tracks')

    ]