"""medicine_service URL Configuration

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
from medicine_info import urls as info_urls
from medicine_supplier import urls as supplier_urls
from medicine_type import urls as type_urls
from medicine_updates import urls as updates_urls

urlpatterns = [
    path("info/", include(info_urls)),
    path("supplier/", include(supplier_urls)),
    path("type/", include(type_urls)),
    path("updates/", include(updates_urls)),
]
