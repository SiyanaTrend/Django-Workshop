from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render

from photos.models import Photo


def photo_add_view(request: Request) -> HttpResponse:
    return render(request, 'photos/photo-add-page.html')

def photo_details_view(request: Request, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'comments': comments,
    }

    return render(request, 'photos/photo-details-page.html', context)

def photo_edit_view(request: Request, pk: int) -> HttpResponse:
    return render(request, 'photos/photo-edit-page.html')

