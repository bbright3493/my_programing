# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from .models import UserProfile, EmailVerifyRecord
from django.contrib.auth.hashers import make_password
from operation.models import *
from utils.email_send import send_register_email, send_mail_test
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import json


# Create your views here.

class IndexView(View):
    #首页
    def get(self, request):
        #取出轮播图
        # all_banners = Banner.objects.all().order_by('index')
        # courses = Course.objects.filter(is_banner=False)[:6]
        # banner_courses = Course.objects.filter(is_banner=True)[:3]
        # course_orgs = CourseOrg.objects.all()[:15]
        # return render(request, 'index.html', {
        #     'all_banners':all_banners,
        #     'courses':courses,
        #     'banner_courses':banner_courses,
        #     'course_orgs':course_orgs
        # })
        return render(request, 'index.html')


class RegisterView(View):

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form":register_form, "msg":"用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            #写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎来到编程实战派，是时候开始学习真正的编程实战技术了"
            user_message.save()

            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request, "register.html", {"register_form":register_form})


class LogoutView(View):
    """
    用户登出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST) #获取表单对象
        if login_form.is_valid(): #表单是否合法
            user_name = request.POST.get("username", "")#获取用户名
            pass_word = request.POST.get("password", "")#获取密码
            user = authenticate(username=user_name, password=pass_word)#查询用户名是否对应该密码
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg":"用户未激活！"})
            else:
                return HttpResponse(json.dumps({"msg": "用户名或密码错误！"}), content_type='application/json')

        else:
            return render(request, "login.html", {"login_form":login_form})