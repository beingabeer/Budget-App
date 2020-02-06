from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [path("", views.project_list, name="list")]

