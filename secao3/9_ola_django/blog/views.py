# from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
    print('posso fazer outras coisas')
    return HttpResponse('blog boladaum')

def exemplo(request):
    print('posso fazer outras coisas')
    return HttpResponse('exemplo boladaum')