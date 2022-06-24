from django.urls import path
from . import views

app_name = 'tweet'

urlpatterns = [
    path('tweet/', views.TC_tweetListView.as_view(), name = 'tweet'),
    path('detail/<int:pk>', views.TC_tweetDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.TC_tweetDeleteView.as_view(), name='delete'),
    path('tweet/create', views.TC_tweetCreateView.as_view(), name='tweet-create'),
    path('good/<int:good_id>', views.good, name='good'),
]
