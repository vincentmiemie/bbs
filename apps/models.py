# -*- coding: utf-8 -*-
from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    """
    用户表：
    id：自增编号
    name：用户名
    password：用户密码
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("name", max_length=10)
    password = models.CharField("password", max_length=30)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'bbs_user'

class Reply(models.Model):
    """
    回复表：
    id：自增编号
    tid：帖子id
    uid ：用户id
    reply_time ：回复时间
    reply_content：回复内容
    """
    id = models.AutoField(primary_key=True)
    tid = models.ForeignKey('Theme', verbose_name="tid", editable=False)
    uid = models.ForeignKey(User, verbose_name="uid", editable=False)
    reply_time = models.DateTimeField("reply_time", null=True, blank=True, default=datetime.datetime.now)
    reply_content = models.CharField("reply_content",max_length=300)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'bbs_reply'


class Theme(models.Model):
    """
    帖子表：
    id：自增编号
    uid：用户id
    title：帖子标题
    theme_content：帖子内容
    post_time：发布时间
    last_reply_id ：最后的回复id
    relay_times：回复次数
    is_set_top：是否置顶
    block：所属板块
    """
    block_choice={
        (0,'C语言'),
        (1,'Python'),
        (2,'Java'),
        (3,'PHP')
    }
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, verbose_name="uid", editable=False)
    title = models.CharField("theme_title", max_length=30)
    theme_content = models.CharField("theme_content",max_length=300)
    post_time = models.DateTimeField("post_time", null=True, blank=True, default=datetime.datetime.now)
    last_reply_id = models.ForeignKey('Reply',verbose_name="last_reply_id",null=True, blank=True, editable=False)
    # last_reply_time = models.DateTimeField("last_reply_time",null=True, blank=True)
    relay_times=models.IntegerField("relay_times",default=0,null=True, blank=True)
    is_set_top=models.IntegerField("is_set_top",default=0,null=True, blank=True)
    block = models.BooleanField(choices=block_choice, default=True)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'bbs_theme'


