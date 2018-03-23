# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class IndexView(View):
    #趣学在线网 首页
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
