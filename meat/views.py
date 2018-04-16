import datetime

from django.contrib.auth import logout as sys_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.forms.models import model_to_dict

from .modules import get_modules
from .forms import ConfigForm
from .models import SystemConfig, Customer, CollectInfo
from .number import get__number


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
    config = SystemConfig.objects.first()
    return render(request, 'meat/sg_partial.html',
                  {"config": config})


def post_sg(request):
    if request.method != "POST":
        return JsonResponse({"code": 403, "message": "非法访问被拒绝"})
    try:
        cust = Customer.objects.get(id_card=request.POST.get("id_card"))
        cust.cust_name = request.POST.get("cust_name")
        cust.mobile = request.POST.get("mobile", cust.mobile)
        cust.address = request.POST.get("address", cust.address)
    except:
        cust = Customer(**{
            "id_card": request.POST.get("id_card"),
            "cust_name": request.POST.get("cust_name"),
            "mobile": request.POST.get("mobile", ""),
            "address": request.POST.get("address", "")
        })
    cust.save()
    sg = {
        "sg_no": get__number("SG"),
        "pay_type": request.POST.get("pay_type", 1),
        "sg_price": request.POST.get("sg_price", 0),
        "sg_datetime": request.POST.get("sg_datetime"),
        "sg_source": request.POST.get("sg_source"),
        "c_type": request.POST.get("c_type"),
        "c_standard": request.POST.get("c_standard"),
        "cz_number": request.POST.get("cz_number"),
        "cz_weight": request.POST.get("cz_weight"),
        "state": 1,
        "flow_step": 1,
        "user": request.user,
        "customer": cust
    }
    model = CollectInfo(**sg)
    model.save()
    return JsonResponse({"code": 200,"message": "本次收购数据提交成功"})


def sg_list(request):
    return render(request, 'meat/sg_list.html')


def get_sgdata(request):
    size = request.GET.get("size", 10)
    page = request.GET.get("page", 0)
    models = CollectInfo.objects.filter(flow_step=1, state=1).order_by("-id")
    data = [m.to_dict() for m in models]
    return JsonResponse(data, safe=False)



def tzq_edit(request):
    config = SystemConfig.objects.first()
    return render(request, 'meat/tzq_edit.html', {"config": config})


def post_tzq(request):
    if request.method != "POST":
        return JsonResponse({"code": 403, "message": "非法访问被拒绝"})
    sg_no = request.POST.get('sg_no', '')
    if len(sg_no) == 0:
        return JsonResponse({"code": 404, "message": "没有找到对应的收购信息，提交失败"})
    try:
        model = CollectInfo.objects.get(sg_no=sg_no, flow_step=1)
        model.tzq_datetime = request.POST.get("tzq_datetime", datetime.datetime.now())
        model.cz_number2 = request.POST.get("cz_number2", 0)
        model.cz_weight2 = request.POST.get("cz_weight2", 0)
        model.user2 = request.user
        model.save()
        return JsonResponse({"code": 200, "message": "数据提交成功"})
    except Exception as e:
        return JsonResponse({"code": 500, "message": "发生错误，提交失败"})


def get_collectInfo_by_sgno(request, no):
    try:
        model = CollectInfo.objects.get(sg_no=no, flow_step=1)
        return JsonResponse({"code": 200, "data": model.to_dict()})
    except:
        return JsonResponse({"code": 404, "data": None})


def tzq_list(request):
    return render(request, 'meat/tzq_list.html')


def ttcz_edit(request):
    config = SystemConfig.objects.first()
    return render(request, 'meat/ttcz_edit.html', {"config": config})


def sys_settings(request):
    config = SystemConfig.objects.first()
    return render(request, 'meat/sys_settings.html', {"config": config})


def post_config(request):
    if request.method == "POST":
        form = ConfigForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = request.POST.get("pk", 0)
            instance.save()
            return JsonResponse({"code": 200, "message": "保存成功"})
    return JsonResponse({"code": 403})
