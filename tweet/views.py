from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TC_tweet

# Create your views here.


class TC_tweetListView(LoginRequiredMixin, ListView):
    model = TC_tweet
    template_name = "tweet/tweet.html"
    context_object_name = "tweets"
    ordering = ["-date_posted"]
    paginate_by: 20

class TC_tweetCreateView(LoginRequiredMixin, CreateView):
    model = TC_tweet
    fields = ['content']
    template_name = "tweet/tweet_create.html"
    success_url = "/tweet"

    #form_valid関数は、データがポストされた時に呼ばれるメソッド
    def form_valid(self, form):
        #投稿者が誰かを教える。
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)
