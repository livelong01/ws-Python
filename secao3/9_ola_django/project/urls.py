"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


# HTTP Request <-> HTTP Response
# MVT (MVC)


def home(request):
    print('HOME')
    return HttpResponse('HOME PAGE')

def blog(request):
    print('posso fazer outras coisas')
    return HttpResponse('blog')

urlpatterns = [
    path('blog/', blog),
    path('', home)
    path('admin/', admin.site.urls),
]
