# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
from users.models import UserProfile


# Create your models here.
class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserQuestionTeacher(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"提问用户")
    question_content = UEditorField(verbose_name=u"提问内容", width=600, height=300, imagePath="operation/ueditor/",
                          filePath="operation/ueditor/")
    answer = UEditorField(verbose_name=u"老师回答",width=600, height=300, imagePath="operation/ueditor/",
                                         filePath="operation/ueditor/")
    question_status = models.IntegerField(choices=((1,"已回答"), (0,"未回答")), default=0, verbose_name=u'是否已经回答')
    user_question_time = models.DateTimeField(default=datetime.now, verbose_name=u"提问时间")
    teacher_answer_time = models.DateTimeField(default=datetime.now, verbose_name=u"回答时间")
    class Meta:
        verbose_name = u'用户问题回答'
        verbose_name_plural = verbose_name