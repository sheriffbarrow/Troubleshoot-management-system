from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import ComplaintForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Complaint


class Index(generic.ListView):
    model = Complaint
    context_object_name = 'books'
    template_name = 'index.html'


class ComplaintCreateView(BSModalCreateView):
    template_name = 'examples/create_book.html'
    form_class = ComplaintForm
    success_message = 'Success: Complaint was created.'
    success_url = reverse_lazy('index')


class ComplaintUpdateView(BSModalUpdateView):
    model = Complaint
    template_name = 'examples/update_book.html'
    form_class = ComplaintForm
    success_message = 'Success: Complaint was updated.'
    success_url = reverse_lazy('index')


class ComplaintReadView(BSModalReadView):
    model = Complaint
    context_object_name = 'book'
    template_name = 'examples/read_book.html'


class ComplaintDeleteView(BSModalDeleteView):
    model = Complaint
    context_object_name = 'book'
    template_name = 'examples/delete_book.html'
    success_message = 'Success: Complaint was deleted.'
    success_url = reverse_lazy('index')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'examples/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'examples/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')
