from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models
from . import forms


class DeviceListView(generic.ListView):
    model = models.Device
    context_object_name = 'device_list'
    template_name = "mobile_devices/device_list.html"

    def get_queryset(self):
        return models.Device.objects.filter().order_by('-id')


class DeviceDetailView(generic.DetailView):
    model = models.Device
    context_object_name = 'device_id'
    template_name = "mobile_devices/device_detail.html"

    def get_object(self, **kwargs):
        device_id = self.kwargs.get("id")
        return get_object_or_404(models.Device, id=device_id)


class DeviceCreateView(generic.edit.CreateView):
    model = models.Device
    form_class = forms.DeviceForm
    template_name = "mobile_devices/device_create.html"
    success_url = "/device_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(DeviceCreateView, self).form_valid(form=form)


class SmartphoneListView(generic.ListView):
    model = models.Device
    context_object_name = 'smartphone_list'
    template_name = "mobile_devices/smartphone_list.html"

    def get_queryset(self):
        return self.model.objects.filter(category__name="Смартфон").order_by("-id")


class TabletListView(generic.ListView):
    model = models.Device
    context_object_name = 'tablet_list'
    template_name = "mobile_devices/tablet_list.html"

    def get_queryset(self):
        return self.model.objects.filter(category__name="Планшет").order_by("-id")


class SmartwatchListView(generic.ListView):
    model = models.Device
    context_object_name = 'smartwatch_list'
    template_name = "mobile_devices/tablet_list.html"

    def get_queryset(self):
        return self.model.objects.filter(category__name="Умные часы").order_by("-id")