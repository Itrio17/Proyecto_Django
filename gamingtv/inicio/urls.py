from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('streamers/', views.streamers, name="streamers"),
    path('streamingroom/', views.streamingroom, name="streamingroom"),
]
