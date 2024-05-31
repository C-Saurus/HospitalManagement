from django.urls import path
from .views import create, update, get_all

urlpatterns = [
    path("<int:id>/update", update, name="update"),
    path("create", create, name="create"),
    path("", get_all, name="get_all")
]