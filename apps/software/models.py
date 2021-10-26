from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from mdeditor.fields import MDTextField

class SoftWare(BaseModel):
    name = models.CharField(verbose_name='软件名称',max_length=50)
    detail = MDTextField(verbose_name='软件详情')
    tag = models.CharField(verbose_name='软件标签',max_length=10,default='')
    image = models.ImageField(verbose_name='封面图',upload_to='software/%Y/%m/%d',max_length=100)
    fake_sales = models.IntegerField(verbose_name='模拟销量',default=199)
    real_sales = models.IntegerField(verbose_name='真实销量',default=0)
    base_price = models.IntegerField(verbose_name='基础价格',default=9999)


    class Meta:
        verbose_name = '软件上架'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class SoftPrice(BaseModel):
    software = models.ForeignKey(SoftWare,on_delete=models.CASCADE,verbose_name='软件名称')
    license_category = models.CharField(verbose_name='套餐类型',choices=(('rl','开通权限'),('el','延长权限')),max_length=10)
    name = models.CharField(verbose_name='套餐名称',max_length=100)
    price = models.IntegerField(verbose_name='套餐价格', default=0)

    class Meta:
        verbose_name = '软件套餐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name