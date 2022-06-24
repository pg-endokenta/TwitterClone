from django.db import models
from django.utils import timezone
from django.conf import settings

from user.models import TC_user
# Create your models here.

class TC_tweet(models.Model):
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content

class Good(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='good_owner')
    tweet = models.ForeignKey(TC_tweet, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.tweet) + '" （by' + str(self.owner) + '）'