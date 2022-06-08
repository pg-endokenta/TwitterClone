#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from .models import tc_user
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
        return response

class LoginView(LoginView):
    template_name = "user/login.html"
    model = tc_user

def LogoutView(request):
    logout(request)
    return redirect('user:login')