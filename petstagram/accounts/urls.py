from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login-page.html'), name='login'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details_view, name='profile-details'),
        path('edit/', views.profile_edit_view, name='edit-profile'),
        path('delete/', views.profile_delete_view, name='delete-profile')
    ])),
]