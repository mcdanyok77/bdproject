"""
URL configuration for labs6_11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main_page, name='main_page'),
    path('outlets/', views.outlets_page, name='outlets'),
    path('outlets/add/', views.add_outlet, name='add_outlet'),
    path('outlets/edit/<int:outlet_id>/', views.edit_outlet, name='edit_outlet'),
    path('outlets/delete/<int:outlet_id>/', views.delete_outlet, name='delete_outlet'),
    path('clients/', views.clients_page, name='clients'),
    path('rent/', views.rent_page, name='rent'), 
    path('monthlypayment/', views.monthlypayment_page, name='monthlypayment'), 
]

