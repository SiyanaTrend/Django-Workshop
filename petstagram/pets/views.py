from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render

from pets.models import Pet


def pet_add_view(request: Request) -> HttpResponse:
    return render(request, 'pets/pet-add-page.html')

def pet_details_view(request: Request, username: str, pet_slug: str) -> HttpResponse:
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.prefetch_related('tagged_pets', 'like_set').all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context)

def pet_edit_view(request: Request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, 'pets/pet-edit-page.html')

def pet_delete_view(request: Request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, 'pets/pet-delete-page.html')

