from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.project_list, name="list"),
    path("add", views.ProjectCreateView.as_view(), name="add"),
    path("<slug:slug>", views.project_detail, name="detail"),
]

