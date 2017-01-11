# coding=utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from apps.models import User
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


# 注册
def regist(request, tmp_name='regist.html'):
    name = request.POST.get("name", "")
    password = request.POST.get("password", "")
    if name.strip() and password.strip():
        try:
            msg = regist_action(name, password)
            messages.add_message(request, messages.INFO, msg)
            logger.info(u"用户:%s注册" % (name))
            return HttpResponseRedirect(reverse('index'))
        except Exception as e:
            logger.error(e.message)
            messages.add_message(request, messages.ERROR, u"注册失败")
    return render_to_response(tmp_name, context_instance=RequestContext(request))


def regist_action(name, password):
    try:
        if User.objects.filter(name=name).exists():
            msg = u"用户名【%s】已经存在，请重新输入，谢谢！" % name
        else:
            pro = User.objects.create(
                name=name,
                password=password,
            )
            logger.info(u"添加新用户:%s" % (name))
            msg = u"您已成功注册【%s】！" % name
        return msg
    except Exception as e:
        raise e


# 登陆
def login(request, tmp_name='login.html'):
    name = request.POST.get("name", "")
    password = request.POST.get("password", "")
    if name.strip() and password.strip():
        try:
            msg = login_check(name, password)
            messages.add_message(request, messages.INFO, msg)
            logger.info(u"用户:%s登陆" % (name))
            return HttpResponseRedirect(reverse('index'))
        except Exception as e:
            logger.error(e.message)
            messages.add_message(request, messages.ERROR, u"登录失败")
    return render_to_response(tmp_name, context_instance=RequestContext(request))


def login_check(name, password):
    try:
        if not User.objects.filter(name=name).exists():
            msg = u"用户名【%s】不存在存在，请重新输入，谢谢！" % name
        else:
            user = User.objects.filter(name__exact=name, password__exact=password)
            if user:
                logger.info(u"%s用户登录" % (name))
                msg = u"【%s】，您已成功登陆！" % name
            else:
                logger.info(u"%s用户登录失败，密码错误" % (name))
                msg = u"【%s】，用户名与密码不符！" % name
        return msg
    except Exception as e:
        raise e


# 登陆成功
def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('index.html', {'username': username})


# 退出
def logout(req):
    response = HttpResponse('logout !!')
    # 清理cookie里保存username
    response.delete_cookie('username')
    return response
