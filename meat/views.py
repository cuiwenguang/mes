from django.contrib.auth import logout as sys_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def logout(request):

    sys_logout(request)
    return redirect(index)

@login_required
def index(request):
    return render(request, 'meat/index.html')


def sg_edit(request):
    return render(request, 'meat/sg_partial.html')
