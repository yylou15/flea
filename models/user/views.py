import datetime

from django.http import HttpResponse
from django.shortcuts import render

from models.user.models import Info

# Create your views here.
def signup(request):
    new_user = Info(openid=123,sex='男',phone=13278886615,createTime=datetime.datetime.now())
    new_user.save()
    return HttpResponse()
