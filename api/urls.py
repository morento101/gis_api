from django.urls import path
from .views import MapListView

urlpatterns = [
    path('maps/', MapListView.as_view(), name='maps'),
]
