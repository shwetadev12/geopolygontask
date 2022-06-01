"""mozio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from mozio_app.views import (
    CreateProviderViewSet,
    GetProviderViewSet,
    UpdateProviderViewSet,
    DeleteProviderViewSet,
    CreateServiceAreaViewSet,
    UpdateServiceAreaViewSet,
    GetServiceAreaViewSet,
    DeleteServiceAreaViewSet,
    GetPolygonsViewSet
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/provider/create', CreateProviderViewSet.as_view()),
    path('api/provider/<int:pk>', GetProviderViewSet.as_view()),
    path('api/provider/update/<int:pk>', UpdateProviderViewSet.as_view()),
    path('api/provider/delete/<int:pk>', DeleteProviderViewSet.as_view()),
    path('api/service-area/create', CreateServiceAreaViewSet.as_view()),
    path('api/service-area/<int:pk>', GetServiceAreaViewSet.as_view()),
    path('api/service-area/update/<int:pk>', UpdateServiceAreaViewSet.as_view()),
    path('api/service-area/delete/<int:pk>', DeleteServiceAreaViewSet.as_view()),
    path('api/polygon', GetPolygonsViewSet.as_view()),
]
