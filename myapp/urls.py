from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexPage, name = "indexpage"),
    path("register/",views.RegisterPage,name="registerpage"),
    path("loginpage/",views.LoginPage, name = "loginpage"),
    path("contactpage/",views.ContactPage,name = "contactpage"),
]