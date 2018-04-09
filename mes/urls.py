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
from meat.views import (index, logout, sys_settings,
                        sg_edit, sg_list, tzq_edit,
                        tzq_list, ttcz_edit)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', sys_login, {'template_name': 'login.html'}),
    path('logout/', logout, name="logout"),
    path('', index),
    path('sys_settings', sys_settings),
    path('sg_edit/', sg_edit),
    path('sg_list/', sg_list),
    path('tzq_edit/', tzq_edit),
    path('tzq_list/', tzq_list),
    path('ttcz_edit/', ttcz_edit),
]
