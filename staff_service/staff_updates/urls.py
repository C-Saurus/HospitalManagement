from django.urls import path
from .views import update_department, update, update_level

urlpatterns = [
    path("<int:id>/update_department", update_department, name="update_department"),
    path("<int:id>/update", update, name="update"),
    path("<int:id>/update_level", update_level, name="update_level"),
]