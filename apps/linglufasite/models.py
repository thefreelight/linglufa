from django.db import models
from apps.users.models import BaseModel

# Create your models here.
#友情链接model
class SiteLink(BaseModel):
    name = models.CharField(max_length=20,verbose_name="网站名称")
    link = models.URLField(verbose_name="网站地址")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#提供服务model
class OurServie(BaseModel):
    title = models.CharField(max_length=20,verbose_name="服务名称")
    image = models.ImageField(upload_to="service_icon/",default='default.svg',verbose_name="服务图标")
    desc = models.CharField(max_length=100,verbose_name="服务描述")

    class Meta:
        verbose_name = "服务管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


#我们的优势
class OurSuperior(BaseModel):
    title = models.CharField(max_length=20, verbose_name="优势名称")
    image = models.ImageField(upload_to="service_icon/", default='default.svg', verbose_name="优势图标")
    desc = models.CharField(max_length=100, verbose_name="优势描述")

    class Meta:
        verbose_name = "优势管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title



