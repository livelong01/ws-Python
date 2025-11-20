from django.shortcuts import render



def blog(request):
    print('posso fazer outras coisas')
    return render(request, 'blog/index.html')

def exemplo(request):
    print('posso fazer outras coisas')
    return render(request, 'blog/exemplo.html')