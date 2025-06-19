from django.urls import path, include

from common import views

urlpatterns = [
    path('', views.home_page_view, name='home-page'),
    path('<int:photo_id>/', include([
        path('like/', views.like, name='like'),
        path('share/', views.share, name='share'),
    ])),
]