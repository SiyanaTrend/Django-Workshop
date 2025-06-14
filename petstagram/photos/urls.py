from django.urls import path, include

from photos import views

urlpatterns = [
    path('add/', views.photo_add_view, name='add-photo'),
    path('<int:pk>/', include([
        path('', views.photo_details_view, name='photo-details'),
        path('edit/', views.photo_edit_view, name='edit-photo'),
    ])),
]