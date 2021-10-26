from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        abstract = True

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,default='',verbose_name='昵称')
    job_name = models.CharField(max_length=50,default='',verbose_name='工作名称')
    job_class = models.CharField(max_length=50,default='',verbose_name='工作种类')
    image = models.ImageField(upload_to="head_image/%Y/%m/%d",default='default.jpg',verbose_name='用户头像')


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username