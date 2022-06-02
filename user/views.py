from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

"""
class SignUpView(CreateView):
    template_name = "user/signup.html"
    model = User
    fields = ('username', 'password')
    success_url = reverse_lazy('twitter:home')
"""
"""
def SignUpView (request):
    #最初はGETでアクセスされる。そのときにエラーメッセージを表示させないための場合わけ
    if request.method =='POST':
        username_date = request.POST['username_date']
        password_date = request.POST['[password_date']
        try:
            User.objects.create_user('username_date', '', 'password_date')
        except IntegrityError:
            return render(request, 'user/signup.html', {'error':'このユーザー名はすでに使われています。'})
    else:
        return render(request, 'user/signup.html', {})
    return render(request, 'user/signup.html', {})
"""

class SignUpView(CreateView):
    template_name = 'user/signup.html'
    form_class = UserCreationForm
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
    model = User

def LogoutView(request):
    logout(request)
    return redirect('user:login')