from django.urls import path
from watchlist_api import views

urlpatterns = [
    path('ott/',views.StreamPlatformList.as_view(),name='ott-platform'),
    path('ott/<int:pk>/',views.StreamPlatformList.as_view(),name='ott-pd'),
    path('watchlist/',views.WatchlistView.as_view(),name='watchlist'),
    path('watchlist/<int:pk>/',views.WatchlistUpdate.as_view(),name='watchlist-update')
]
