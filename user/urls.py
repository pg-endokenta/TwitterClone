from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path("login/", views.LoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutView, name = 'logout'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name = 'profile'),
    path('profile/update/<int:pk>', views.ProfileUpdateView.as_view(), name = 'profile_update'),
]
