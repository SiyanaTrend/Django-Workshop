from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render, redirect

from common.models import Like
from photos.models import Photo


def home_page_view(request: Request) -> HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets', 'like_set').all()

    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html', context)


def like(request, photo_id: int) -> HttpResponse:
    like_object = Like.objects.filter(to_photo_id=photo_id).first()

    if like_object:
        like_object.delete()
    else:
        Like.objects.create(
            to_photo_id=photo_id
        )

    return redirect(request.META.get('HTTP_REFERER') + f"#{photo_id}")
