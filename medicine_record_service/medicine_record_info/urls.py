from django.urls import path
from .views import item_list, item_detail

urlpatterns = [
    # GET APIs
    path('', item_list),
    path('<int:id>', item_detail),
]