from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from common.forms import CommentForm
from common.mixins import UserIsOwnerMixin
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


class PhotoAddView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# def photo_add_view(request: HttpRequest) -> HttpResponse:
#     form = PhotoCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('home-page')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'photos/photo-add-page.html', context)


class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comments': self.object.comment_set.all(),
            'comment_form': CommentForm(),
        })
        return super().get_context_data(**kwargs)


# def photo_details_view(request: HttpRequest, pk: int) -> HttpResponse:
#     photo = Photo.objects.get(pk=pk)
#     comments = photo.comment_set.all()
#     comment_form = CommentForm()
#
#     context = {
#         'photo': photo,
#         'comments': comments,
#         'comment_form': comment_form,
#     }
#
#     return render(request, 'photos/photo-details-page.html', context)


class PhotoEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse('photo-details', kwargs={'pk': self.object.pk})


# def photo_edit_view(request: HttpRequest, pk: int) -> HttpResponse:
#     photo = Photo.objects.get(pk=pk)
#     form = PhotoEditForm(request.POST or None, instance=photo)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('photo-details', pk=pk)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'photos/photo-edit-page.html', context)


@login_required
def photo_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)

    if request.user.pk == photo.user.pk:
        photo.delete()
        return redirect('home')

    return HttpResponseForbidden()
