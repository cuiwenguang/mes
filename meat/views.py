from django.contrib.auth import logout as sys_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http.response import JsonResponse


from .modules import get_modules
from .forms import ConfigForm
from .models import SystemConfig


def logout(request):
    sys_logout(request)
    return redirect(index)


@login_required
def index(request):
    modules = get_modules(request.user, 0)
    return render(request, 'meat/index.html', context={
        "modules": modules
    })


def sg_edit(request):
    return render(request, 'meat/sg_partial.html')


def sg_list(request):
    return render(request, 'meat/sg_list.html')


def tzq_edit(request):
    return render(request, 'meat/tzq_edit.html')


def tzq_list(request):
    return render(request, 'meat/tzq_list.html')


def ttcz_edit(request):
    return render(request, 'meat/ttcz_edit.html')


def sys_settings(request):
    return render(request, 'meat/sys_settings.html')


def config_save(request):
    if request.method == "POST":
        conf_form = ConfigForm(request.POST)
        if not conf_form.is_valid():
            return JsonResponse({
                "code": 403,
                "message": "非法数据提交"
            })
        conf_form.save()