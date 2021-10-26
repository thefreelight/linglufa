from django.contrib import admin

from apps.software.models import SoftWare,SoftPrice

class SoftWareAdmin(admin.ModelAdmin):
    list_display = ['name','tag','add_time']
    search_fields = ['name','tag']
    list_filter = ['tag']
    list_editable = ['tag']

class SoftPriceAdmin(admin.ModelAdmin):
    list_display = ['software','name', 'license_category','price', 'add_time']
    search_fields = ['name']
    list_filter = ['license_category']
    list_editable = ['price','license_category']

admin.site.register(SoftWare,SoftWareAdmin)
admin.site.register(SoftPrice,SoftPriceAdmin)
