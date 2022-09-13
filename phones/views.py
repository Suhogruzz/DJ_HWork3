from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_by = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_param = request.GET.get('sort')
    if sort_param:
        phones = phones.order_by(sort_by[sort_param])

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
