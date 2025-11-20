from django.shortcuts import render


def home(request):
    print('HOME')
    return render(request, 'home/index.html')