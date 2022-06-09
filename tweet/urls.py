from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('tweet/', views.TC_tweetListView.as_view(), name = 'tweet'),
    path('tweet/create', views.TC_tweetCreateView.as_view(), name='tweet-create'),
]
