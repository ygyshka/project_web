from django.shortcuts import render
from django.views.generic import TemplateView

from catalog.models import Product


# Create your views here.

# def contacts(request):
#     print(request.method)
#     if request.method == "POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}): {message}')
#
#     return render(request, 'catalog/contacts.html')

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


def home(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'catalog/home.html', context)


def product(request, pk):
    product_ = Product.objects.get(id=pk)
    context = {
        'object': product_,
    }

    return render(request, 'catalog/product.html', context)


