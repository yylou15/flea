from django.db import models


# Create your models here.
class Cate(models.Model):
    cid = models.AutoField(primary_key=True, default=None)
    cateName = models.CharField(max_length=20)
    count = models.IntegerField()

class Info(models.Model):
    gid = models.AutoField(primary_key=True,default=None)
    caption = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=2)
    createTime = models.DateField()
    belongCate = models.ForeignKey(Cate, related_name='good_cate', default=0,on_delete=models.CASCADE,to_field='cid')
    owner = models.ForeignKey("user.Info",related_name='good_user',default=0,on_delete=models.CASCADE, to_field='uid')
    soldTime = models.DateField()
    status = models.CharField(max_length=10)
