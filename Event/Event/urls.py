"""
URL configuration for Event project.

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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('adminPage/',views.admin),
    path('register/',views.register),
    path('login/',views.login),
    path('viewUser/',views.viewUser),
    path('delete/<int:id>',views.delete),
    path('mainPage/',views.mainPage),
    path('update/<int:id>',views.update),
    path('gold/',views.gold),
    path('plat/',views.plat),
    path('diamond/',views.diamond),
    path('about/',views.about),
    path('logOut/',views.logOut),
    path('addCategory/',views.addCategory),
    path('viewCategory/',views.viewCategory),
    path('updateCategory/<int:id>',views.updateCategory),
    path('deleteCategory/<int:id>',views.deleteCategory),
    path('choosePlan/<int:id>',views.choosePlan),
    path('viewRequest/',views.viewRequest),
    path('approve/<int:id>',views.approve),
    path('reject/<int:id>',views.reject),
    path('myEvent/',views.myEvent),
    path('payment/<int:id>/<str:event_name>/<pr>',views.payment),
    path('history/',views.history),
    


    
    


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)