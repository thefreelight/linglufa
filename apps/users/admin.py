from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile



class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserAdmin)

#后台管理系统左上角改名
admin.site.site_title = '领路发后台'
admin.site.site_header = '领路发后台管理系统'
