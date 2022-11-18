from django.contrib import admin
from django.urls import path
from . import views

app_name = 'place'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('place/detail/'), # 플레이스 리스트
    path('place/detail/<int:restaurant_id>/', views.PlaceDetailView.as_view(), name='place-detail')
]