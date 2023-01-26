from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "teams"

urlpatterns = [
    
    path("createTeam", views.create_team, name="createTeam"),

]