from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class TC_user(AbstractUser):
    class Meta:
        #Userモデルのテーブル名を指定
        db_table = 'TC_user'


class TC_profile(models.Model):
    SelfIntroduction = models.CharField(verbose_name="自己紹介",max_length=200, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)


class Follow(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follow_owner')
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return 'follow for "' + str(self.followed) + '" （by' + str(self.owner) + '）'