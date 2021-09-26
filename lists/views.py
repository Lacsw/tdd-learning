from django.http.response import HttpResponse
from django.shortcuts import render

def home_page(request):
    """"домашняя страница"""
    return HttpResponse('<html><title>To-Do lists</title></html>')