from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = models.Developer
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "salary",
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.salary = self.cleaned_data["salary"]
        if commit:
            user.save()
        return user
