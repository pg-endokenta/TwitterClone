from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "twitter/home.html"

