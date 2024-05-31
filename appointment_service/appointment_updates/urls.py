from django.urls import path
from .views import delete, update

urlpatterns = [
    path("<int:id>/update", update, name="update"),
    path("<int:id>/delete", delete, name="delete"),
]