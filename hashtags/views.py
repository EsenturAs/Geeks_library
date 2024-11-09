from django.shortcuts import render
from . import models


def all_products_list_view(request):
    if request.method == 'GET':
        products_list = models.Product.objects.filter().order_by('-id')
        context = {'products_list': products_list}
        return render(request, 'all_products_list.html',
                      context=context)


def for_elder_view(request):
    if request.method == 'GET':
        elder_products = models.Product.objects.filter(tags__age="Пристарелые").order_by('-id')
        context = {'elder_products': elder_products}
        return render(request, 'elder.html',
                      context=context)


def for_young_view(request):
    if request.method == 'GET':
        for_young = models.Product.objects.filter(tags__age="Молодые").order_by('-id')
        context = {'for_young': for_young}
        return render(request, 'young.html',
                      context=context)


def for_kids_view(request):
    if request.method == 'GET':
        for_kids = models.Product.objects.filter(tags__age="Дети").order_by('-id')
        context = {'for_kids': for_kids}
        return render(request, 'kids.html',
                      context=context)