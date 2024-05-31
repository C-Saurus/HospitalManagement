from django.urls import path
from .views import create, get_all, get_detail, update

urlpatterns = [
    path("<int:id>", get_detail, name="get_detail"),
    path("<int:id>/update", update, name="update"),
    path("create", create, name="create"),
    path("", get_all, name="get_all")
]