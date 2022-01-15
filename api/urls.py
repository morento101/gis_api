from django.urls import path
from .views import MapListView, ChainListView, LineListView, PointListView

urlpatterns = [
    path('maps/', MapListView.as_view(), name='maps'),
    path('chains/', ChainListView.as_view(), name='chains'),
    path('lines/', LineListView.as_view(), name='lines'),
    path('points/', PointListView.as_view(), name='points'),
]
