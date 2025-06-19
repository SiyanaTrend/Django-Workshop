from urllib.request import Request

from django.http import HttpResponse
from django.shortcuts import render

from photos.models import Photo


def home_page_view(request: Request) -> HttpResponse:
    all_photos = Photo.objects.prefetch_related('tagged_pets').all()

    context = {
        'all_photos': all_photos,
    }
    return render(request, 'common/home-page.html', context)


