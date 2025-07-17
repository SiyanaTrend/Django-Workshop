from django.contrib.auth import get_user_model, login
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import AppUserCreationForm

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

def profile_edit_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-edit-page.html')

def profile_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'accounts/profile-delete-page.html')

