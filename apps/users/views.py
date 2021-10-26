from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import LoginForm,DynamicLoginForm,RegisterGetForm,RegForm
from apps.users.models import UserProfile

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        login_form = DynamicLoginForm()
        return render(request, 'login.html',{
            "login_form":login_form
        })

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {"msg": "用户名或密码错误","login_form":login_form})
        else:
            return render(request, 'login.html', {'login_form':login_form})

class RegView(View):
    def get(self, request, *args, **kwargs):
        register_get_form = RegisterGetForm()
        return render(request, 'register.html',{
            "register_get_form":register_get_form,
        })
    def post(self, request, *args, **kwargs):
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data["username"]
            password = reg_form.cleaned_data['password']
            #新建一个用户
            user = UserProfile(username=username)
            user.set_password(password)
            user.username = username
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            register_get_form = RegisterGetForm()
            return render(request, 'register.html', {
                "register_get_form": register_get_form,
                "reg_form":reg_form
            })

