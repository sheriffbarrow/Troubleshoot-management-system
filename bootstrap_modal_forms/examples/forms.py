from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Complaint


class ComplaintForm(BSModalForm):

    class Meta:
        model = Complaint
        exclude = ['date_time']
        widgets = {
          'additional_Info': forms.Textarea(attrs={'rows':3, 'cols':10}),
        }


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
