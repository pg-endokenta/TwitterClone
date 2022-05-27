from django.shortcuts import render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = "user/signup.html"

class LoginView(TemplateView):
    template_name = "user/login.html"