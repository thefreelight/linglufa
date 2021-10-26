"""linglufa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from apps.users.views import LoginView, LogoutView,ProfileView,RegView
from apps.linglufasite.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/',ProfileView.as_view(),name='profile'),
    url(r'mdeditor/', include('mdeditor.urls')), #配置md编辑器
    path('reg/',RegView.as_view(),name='reg'),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)