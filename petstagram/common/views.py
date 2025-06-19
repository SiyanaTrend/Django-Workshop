from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from common.models import Like
from photos.models import Photo


def home_page_view(request: Request) -> HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()

    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html', context)


def like(request: Request, photo_id: int) -> HttpResponse:
    like_object = Like.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id
        )

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")

def share(request: Request, photo_id: int) -> HttpResponse:
    # pip install pyperclip
    # this will only work locally
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")


