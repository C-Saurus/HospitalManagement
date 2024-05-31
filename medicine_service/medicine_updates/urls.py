from django.urls import path
from .views import delete, update, update_quantity

urlpatterns = [
    path("<int:id>/update", update, name="update"),
    path("<int:id>/update_quantity", update_quantity, name="update_quantity"),
    path("<int:id>/delete", delete, name="delete"),
]