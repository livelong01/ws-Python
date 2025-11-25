from django.shortcuts import render


def home(request):
    print('HOME')
    return render(request, 'home/index.html')
    # return render(request, 'global/base.html')