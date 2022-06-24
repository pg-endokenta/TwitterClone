from ast import Param
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from user.models import TC_profile


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "twitter/home.html"

    #変数を渡す
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["username"] = user
        context["self_introduction"] = user.tc_profile.SelfIntroduction
        context["profile_id"] = user.tc_profile.pk

        #pk = request.user.pk
        #my_profile = TC_profile.objects.get(pk=pk)
        #context["self_introduction"] = my_profile.SelfIntroduction
        return context