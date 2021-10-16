from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('', views.index, name="login"),
    path('register',views.register_request, name="register"),
]
