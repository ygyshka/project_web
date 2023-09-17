from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import Product


# Create your views here.

def contacts(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog/contacts.html')


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
