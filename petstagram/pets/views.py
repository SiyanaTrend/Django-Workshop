from urllib.request import Request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from common.forms import CommentForm
from common.mixins import UserIsOwnerMixin
from pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from pets.models import Pet


class PetAddView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetCreateForm
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})
    template_name = 'pets/pet-add-page.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


# def pet_add_view(request: HttpRequest) -> HttpResponse:
#     form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('profile-details', pk=1)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'pets/pet-add-page.html', context)



class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
            'all_photos': self.object.photo_set.prefetch_related('tagged_pets', 'like_set').all(),
        })
        return super().get_context_data(**kwargs)

# def pet_details_view(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     all_photos = pet.photo_set.prefetch_related('tagged_pets', 'like_set').all()
#     comment_form = CommentForm()
#
#     context = {
#         'pet': pet,
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#     }
#
#     return render(request, 'pets/pet-details-page.html', context)


class PetEditView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'

    def get_success_url(self):
        return reverse(
            'pet-details',
            kwargs={
                'username': self.kwargs.get('username'),
                'pet_slug': self.kwargs.get('pet_slug'),
            })


# def pet_edit_view(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return redirect('pet-details', username=username, pet_slug=pet_slug)
#
#     context = {
#         'pet': pet,
#         'form': form,
#     }
#
#     return render(request, 'pets/pet-edit-page.html', context)


class PetDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_initial(self) -> dict:
        return self.object.__dict__

    # option 1: fill the form with the data from db and delete it
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


    # option 2: fill the form with the data from db and delete it
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({'data': self.get_initial()})
    #     return kwargs

# def pet_delete_view(request: HttpRequest, username: str, pet_slug: str) -> HttpResponse:
#     pet = Pet.objects.get(slug=pet_slug)
#     form = PetDeleteForm(instance=pet)
#
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('profile-details', pk=1)
#
#     context = {
#         'pet': pet,
#         'form': form
#     }
#
#     return render(request, 'pets/pet-delete-page.html', context)
#
