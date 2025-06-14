from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render

def register_view(request: Request) -> HttpResponse:
    return render(request, 'accounts/register-page.html')

def login_view(request: Request) -> HttpResponse:
    return render(request, 'accounts/login-page.html')

def profile_details_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-details-page.html')

def profile_edit_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-edit-page.html')

def profile_delete_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-delete-page.html')

