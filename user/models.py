from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.

class TC_user(AbstractUser):
    class Meta:
        #Userモデルのテーブル名を指定
        db_table = 'TC_user'


"""
class TC_profile(models.Model)
    SelfIntroduction = models.CharField(verbose_name="自己紹介",max_length=200)
    user    = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="ユーザー",on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.user
"""