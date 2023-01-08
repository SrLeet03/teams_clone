from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"   


urlpatterns = [
    # path("", views.homepage, name="homepage"),
    # ...
    path("register", views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.home, name='home'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),    
]