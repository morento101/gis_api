from django.urls import path
from .views import (
    MapListView, MapDetailView, 
    ChainListView, ChainDetailView,
    LineListView, LineDetailView,
    PointListView, PointDetailView, PointCreateView
)

urlpatterns = [
    path('maps/', MapListView.as_view(), name='maps'),
    path('map/<int:pk>/', MapDetailView.as_view(), name='detail-map'),
    path('chains/', ChainListView.as_view(), name='chains'),
    path('chain/<int:pk>/', ChainDetailView.as_view(), name='detail-chain'),
    path('lines/', LineListView.as_view(), name='lines'),
    path('line/<int:pk>/', LineDetailView.as_view(), name='detail-line'),
    path('points/', PointListView.as_view(), name='points'),
    path('point/<int:pk>/', PointDetailView.as_view(), name='detail-point'),
    path('create-point/', PointCreateView.as_view(), name='create-point')
]
