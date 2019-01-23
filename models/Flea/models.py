from django.db import models

# Create your models here.
class UserInfo(models.Model):
    openid = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    sex = models.CharField(max_length=12)
