#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django import forms
from apps.models import User
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

#登陆成功
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})