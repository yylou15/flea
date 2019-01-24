from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uid = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    sex = models.CharField(max_length=12)
    createTime = models.DateField()
    wxNickName = models.CharField(max_length=50)
    avatarUrl = models.CharField(max_length=150)

class UserMessages(models.Model):
    content = models.CharField(max_length=500)
    status = models.CharField(max_length=6)
    time = models.DateField()
    type = models.IntegerField()
    fromUser = models.ForeignKey(UserInfo,related_name="user_message1", to_field="uid", on_delete=models.CASCADE,default=1)
    toUser = models.ForeignKey(UserInfo,related_name="user_message2", to_field="uid", on_delete=models.CASCADE,default=1)
