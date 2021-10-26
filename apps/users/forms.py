from django import forms
from captcha.fields import CaptchaField

from apps.users.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)



class DynamicLoginForm(forms.Form):
    captcha = CaptchaField()

class RegisterGetForm(forms.Form):
    captcha = CaptchaField()

class RegForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)

    def clean_username(self):
        username = self.data.get("username")
        users = UserProfile.objects.filter(username=username)
        if users:
            raise forms.ValidationError("该用户名已注册")
        return username