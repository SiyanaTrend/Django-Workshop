from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from accounts.forms import AppUserCreationForm, ProfileEditForm
from accounts.models import Profile

UserModel = get_user_model()

class RegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        response = super().form_valid(form)

        if response.status_code in [301, 302]:
            login(self.request, self.object)

        return response


def profile_details_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-details-page.html')

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self) -> str:
        return reverse(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )

def profile_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-delete-page.html')

