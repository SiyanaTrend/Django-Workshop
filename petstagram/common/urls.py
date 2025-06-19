from django.urls import path

from common import views

urlpatterns = [
    path('', views.home_page_view, name='home-page'),
    path('like/<int:photo_id>/', views.like, name='like'),
]