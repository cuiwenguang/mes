"""mes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth.views import login as sys_login
from django.urls import path,re_path
from meat.views import (index, logout, sys_settings, post_config, get_sgdata,get_ttcz, ttcz_list,
                        sg_edit, sg_list, post_sg, tzq_edit, get_collectInfo_by_sgno,
                        post_tzq, ttcz_edit, post_ttcz, pscz_edit)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', sys_login, {'template_name': 'login.html'}),
    path('logout/', logout, name="logout"),
    path('', index),
    path('sys_settings', sys_settings, name="sys_settings"),
    path('post_config', post_config),
    path('sg_edit/', sg_edit, name="sg_edit"),
    path('get_sgdata', get_sgdata),
    path('post_sg', post_sg),
    path('get_sg/<no>',get_collectInfo_by_sgno),
    path('sg_list/', sg_list, name="sg_list"),
    path('tzq_edit/', tzq_edit, name="tzq_edit"),
    path('post_tzq', post_tzq),
    path('ttcz_edit/', ttcz_edit, name="ttcz_edit"),
    path('ttcz_list/', ttcz_list, name="ttcz_list"),
    path('get_ttcz/', get_ttcz, name="get_ttcz"),
    path('post_ttcz', post_ttcz, name="post_ttcz"),
    path('pscz_eidt', pscz_edit, name="pscz_edit"),
]
