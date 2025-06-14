from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render

def pet_add_view(request: Request) -> HttpResponse:
    return render(request, 'pets/pet-add-page.html')

def pet_details_view(request: Request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, 'pets/pet-details-page.html')

def pet_edit_view(request: Request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, 'pets/pet-edit-page.html')

def pet_delete_view(request: Request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, 'pets/pet-delete-page.html')

