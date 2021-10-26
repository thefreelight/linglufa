from django.contrib import admin

# Register your models here.
from apps.linglufasite.models import SiteLink, OurServie,OurSuperior

class SiteLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link','add_time']
    search_fields = ['name']
    list_editable = ['link']

class OurServiceAdmin(admin.ModelAdmin):
    list_display = ['title','desc']
    search_fields = ['title','desc']
    list_editable = ['desc']

class OurSuperiorAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']
    search_fields = ['title', 'desc']
    list_editable = ['desc']


admin.site.register(SiteLink, SiteLinkAdmin)
admin.site.register(OurServie, OurServiceAdmin)
admin.site.register(OurSuperior, OurSuperiorAdmin)

