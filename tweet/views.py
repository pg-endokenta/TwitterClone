from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TC_tweet, Good
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


class TC_tweetListView(LoginRequiredMixin, ListView):
    model = TC_tweet
    template_name = "tweet/tweet.html"
    context_object_name = "tweets"
    ordering = ["-date_posted"]
    paginate_by: 20

class TC_tweetDetailView(LoginRequiredMixin, DetailView):
    template_name = 'tweet/detail.html'
    model = TC_tweet

class TC_tweetDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tweet/delete.html'
    model = TC_tweet
    success_url = "/tweet"

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

def good(request, good_id):
    good_tweet = TC_tweet.objects.get(id=good_id)
    is_good = Good.objects.filter(owner=request.user) \
        .filter(tweet=good_tweet).count()
    if is_good > 0:
        good_tweet.likes -= 1
        good_tweet.save()
        good = Good()
        Good.objects.filter(owner=request.user).filter(tweet=good_tweet).delete()
        messages.success(request, 'いいねを取り消しました')
        return redirect(to='/tweet')
    good_tweet.likes += 1
    good_tweet.save()
    good = Good()
    good.owner = request.user
    good.tweet = good_tweet
    good.save()
    messages.success(request, 'いいねしました')
    return redirect(to='/tweet')
