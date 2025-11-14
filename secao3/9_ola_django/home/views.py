# from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    print('HOME')
    return HttpResponse('HOME PAGE DO APP!')