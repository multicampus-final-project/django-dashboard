"""recycle_userweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import recycle.views as recycle_views
import user.views as user_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    # path('', user_views.index, name='user'),
    # path('accounts/', include('allauth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    path('logout/', user_views.logout, name='logout'),

    path('', recycle_views.index, name='index'),
    path('foliummap/', recycle_views.foliummap),
    path('chart/',recycle_views.chart, name='chart'),
    path('table/',recycle_views.table, name='table'),
    path('machinelist/',recycle_views.machine_list, name='machinelist'),
    path('machineinfo/',recycle_views.machine_info, name='machineinfo'),
    path('partnerlist/',recycle_views.partner_list, name='partnerlist'),
]
