# Generated by Django 2.1.5 on 2019-01-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('openid', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('sex', models.CharField(max_length=12)),
                ('createTime', models.DateField()),
                ('wxNickName', models.CharField(max_length=50)),
                ('avatarUrl', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='UserMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=6)),
                ('time', models.DateField()),
                ('type', models.IntegerField()),
            ],
        ),
    ]