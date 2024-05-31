from django.urls import path
from .views import create_item, update_item, delete_item
urlpatterns = [
    path('create', create_item),
    path('<int:id>/update', update_item),
    path('<int:id>/delete', delete_item),
]