"""staff_service URL Configuration

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
from django.urls import path, include
from staff_model import urls as info_urls
from staff_deparment import urls as department_urls
from staff_role import urls as role_urls
from staff_updates import urls as updates_urls

urlpatterns = [
    path("info/", include(info_urls)),
    path("department/", include(department_urls)),
    path("role/", include(role_urls)),
    path("updates/", include(updates_urls)),
]
