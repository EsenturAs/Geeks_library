from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from . import models, forms


def make_an_order_view(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = forms.BasketForm()
    return render(request, template_name='basket/make_an_order.html', context={'form': form})


def order_list_view(request):
    if request.method == 'GET':
        order_list = models.Order.objects.filter().order_by('-id')
        context = {'order_list': order_list}
        return render(request, template_name='basket/order_list.html', context=context)


def update_order_view(request, id):
    order_id = get_object_or_404(models.Order, id=id)
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, instance=order_id)
        if form.is_valid():
            form.save()
            return HttpResponse("Успешно изменено")
    else:
        form = forms.BasketForm(instance=order_id)
    return render(request, template_name='basket/update_order.html', context={'form': form, 'order_id': order_id})


def delete_order_view(request, id):
    drop_order = get_object_or_404(models.Order, id=id)
    drop_order.delete()
    return HttpResponse("Успешно удалено")