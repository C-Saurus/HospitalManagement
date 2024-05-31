from django.urls import path
from .views import create, update, get_all, get_by_patient_id

urlpatterns = [
    path("<int:id>/update", update, name="update"),
    path("create", create, name="create"),
    path("", get_all, name="get_all"),
    path("<int:id>/patient", get_by_patient_id, name="get_by_patient_id")
]