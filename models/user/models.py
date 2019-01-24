from django.db import models


# Create your models here.
class Info(models.Model):
    uid = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    sex = models.CharField(max_length=12)
    createTime = models.DateField()
    wxNickName = models.CharField(max_length=50)
    avatarUrl = models.CharField(max_length=150)


class Messages(models.Model):
    mid = models.AutoField(primary_key=True, default=None)
    content = models.CharField(max_length=500)
    status = models.CharField(max_length=6)
    time = models.DateField()
    type = models.IntegerField()
    fromUser = models.ForeignKey(Info, related_name="user_message1", to_field="uid", on_delete=models.CASCADE,
                                 default=None)
    toUser = models.ForeignKey(Info, related_name="user_message2", to_field="uid", on_delete=models.CASCADE,
                               default=None)


class Collection(models.Model):
    cid = models.AutoField(primary_key=True, default=None)
    good = models.ForeignKey("goods.Info", related_name="user_collection", to_field='gid', on_delete=models.CASCADE)
    collectTime = models.DateField()


class Order(models.Model):
    oid = models.AutoField(primary_key=True, default=None)
    owner = models.ForeignKey(Info, to_field='uid', default=None, on_delete=models.CASCADE, related_name='user_order1')
    buyer = models.ForeignKey(Info, to_field='uid', default=None, on_delete=models.CASCADE, related_name='user_order2')
    good = models.ForeignKey("goods.Info", to_field='gid', default=None, on_delete=models.CASCADE,
                             related_name='user_order3')
    creatTime = models.DateField()
    status = models.CharField(max_length=10)
    endTime = models.DateField()
    comment = models.CharField(max_length=200)


class ViewRecord(models.Model):
    rid = models.AutoField(primary_key=True, default=None)
    user = models.ForeignKey(Info, to_field='uid', on_delete=models.CASCADE, default=None, related_name='user_record1')
    good = models.ForeignKey("goods.Info", to_field='gid', on_delete=models.CASCADE, default=None,
                             related_name='user_record2')
    time = models.DateField()
