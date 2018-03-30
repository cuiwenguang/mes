from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'meat/index.html')


def sg_edit(request):
    return render(request, 'meat/sg_partial.html')
