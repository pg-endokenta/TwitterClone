#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from urllib import request, response
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from .models import TC_user, TC_profile
from .forms import TC_UserCreationForm

class SignUpView(CreateView):
    template_name = 'user/signup.html'
    form_class = TC_UserCreationForm
    success_url = reverse_lazy('twitter:home')
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        #ユーザー作成と同時にprofileモデルも作成
        my_profile = TC_profile(user = self.request.user)
        my_profile.save()
        return response

class LoginView(LoginView):
    template_name = "user/login.html"
    model = TC_user

def LogoutView(request):
    logout(request)
    return redirect('user:login')

class ProfileDetailView(DetailView):
    model = TC_profile
    context_object_name = "profile"
    template_name = "user/profile.html"
