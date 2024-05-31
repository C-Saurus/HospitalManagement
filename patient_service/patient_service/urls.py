"""patient_service URL Configuration

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
from patient_info import urls as info_urls
from patient_status import urls as status_urls
from patient_type import urls as type_urls
from patient_updates import urls as updates_urls
from patient_rent_info import urls as rent_info_urls

urlpatterns = [
    path("info/", include(info_urls)),
    path("status/", include(status_urls)),
    path("type/", include(type_urls)),
    path("updates/", include(updates_urls)),
    path("rent_info/", include(rent_info_urls)),
]
