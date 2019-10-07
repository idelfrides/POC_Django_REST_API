"""test_REST_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
-----------------------------------------------------

 --> this urls sonfiguration is only about  django REST framework

"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User, Group
from restapi_app.api import viewsets  
from rest_framework import routers  
from restapi_app.views import resthome


router = routers.DefaultRouter()
router.register('users', viewsets.UserViewSet)
router.register('groups', viewsets.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', resthome, name='url_home'),
    path('api-rest/', include(router.urls)),
]

