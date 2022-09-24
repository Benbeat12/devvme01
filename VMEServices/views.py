from django.shortcuts import render, redirect, get_object_or_404
from VMEServices.models import Service, Product


def service_index(request):
    services = Service.objects.all()
    return render(request, 'service_index.html', context={"services": services})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html', context={"service": service})



def product_index(request):
    products = Product.objects.all()
    return render(request, "p_index.html", context={"products": products});


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'detail.html', context={"product": product});
