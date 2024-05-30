from django.urls import path
from .views import update_status

urlpatterns = [
    path("<int:id>/update_status", update_status, name="update_status"),
]