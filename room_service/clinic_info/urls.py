from django.urls import path
from .views import delete, update, get_all, get_detail, update_status, create

urlpatterns = [
    path("<int:id>", get_detail, name="get_detail"),
    path("", get_all, name="get_all"),
    path("create", create, name="create"),
    path("<int:id>/update", update, name="update"),
    path("<int:id>/update_status", update_status, name="update_status"),
    path("<int:id>/delete", delete, name="delete"),
]