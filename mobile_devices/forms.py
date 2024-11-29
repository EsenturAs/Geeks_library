from django import forms
from . import models


class DeviceForm(forms.ModelForm):
    class Meta:
        model = models.Device
        fields = "__all__"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(OrderView, self).form_valid(form=form)
