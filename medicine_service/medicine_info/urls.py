from django.urls import path
from .views import create, get_all, get_detail

urlpatterns = [
    path("<int:id>", get_detail, name="get_detail"),
    path("create", create, name="create"),
    path("", get_all, name="get_all")
]