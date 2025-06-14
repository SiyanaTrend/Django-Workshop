from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render

def photo_add_view(request: Request) -> HttpResponse:
    return render(request, 'photos/photo-add-page.html')

def photo_details_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'photos/photo-details-page.html')

def photo_edit_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'photos/photo-edit-page.html')

