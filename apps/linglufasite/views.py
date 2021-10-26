from django.shortcuts import render
from django.views import View


# Create your views here.
from apps.software.models import SoftWare, SoftPrice
from apps.linglufasite.models import OurServie, SiteLink,OurSuperior


class IndexView(View):
    def get(self, request, *args, **kwargs):
        software = SoftWare.objects.all()
        softprice = SoftPrice.objects.all()
        sitelink = SiteLink.objects.all()
        ourservice = OurServie.objects.all()
        oursuperior = OurSuperior.objects.all()
        return render(request, 'index.html',{
            'software':software,
            'softprice':softprice,
            'sitelink':sitelink,
            'ourservice':ourservice,
            'oursuperior':oursuperior
        })