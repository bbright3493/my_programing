# -*- coding: utf-8 -*-
__author__ = 'bb'
__date__ = '2018/3/25'
from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile
from operation.models import UserQuestionTeacher
from  DjangoUeditor.forms import  UEditorModelForm


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)




class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name']


class UserQuestionTeacherForm(UEditorModelForm):
     class Meta:
        model = UserQuestionTeacher
        fields = ['question_content']