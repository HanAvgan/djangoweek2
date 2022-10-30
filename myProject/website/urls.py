"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from taki import views as takiViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', takiViews.index),
    path('index', takiViews.index),
    path('about_us', takiViews.about_us),
    path('cart', takiViews.cart),
    path('compair', takiViews.compair),
    path('contact', takiViews.contact),
    path('forget_password', takiViews.forget_password),
    path('fourcol', takiViews.fourcol),
    path('general', takiViews.general),
    path('gridview', takiViews.gridview),
    path('listview', takiViews.listview),
    path('login', takiViews.login),
    path('product_details', takiViews.product_details),
    path('products', takiViews.products),
    path('register', takiViews.register),
    path('threecol', takiViews.threecol),
]
