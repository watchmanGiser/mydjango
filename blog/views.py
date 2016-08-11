# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def hello(self):
    return HttpResponse("hello")

def fuc_welc(self):
    html_str = "<html><body><h1>Welcome to here,building!这是一个django项目</h1></body></html>"
    return  HttpResponse(html_str)
