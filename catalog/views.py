from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from catalog.services import get_category_cache


# Create your views here.
@login_required
def contacts(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog/contacts.html')

# Пример реализации вывода списка продуктов на страницу пользователю,
# с дополнительным закрытием доступа не авторирзованным пользователям

# Сделан вывод списка продуктов на страницу через FBV так как на момент решения задачи было не ясно,
# как сделать такое через CBV
# @login_required(login_url='users/') - декоратор для проверки прав доступа для залогиненых пользователей
## @login_required
## def home_list_view(request):
##     product_list = Product.objects.all()
##     context = {
##         'product_list': product_list
##     }
##     return render(request, 'catalog/home.html', context)
# LoginRequiredMixin - базовый класс миксин для проверки аутентифицирован ли пользователь или нет(вошел в систему или нет)

#$def category_list_view(request):
##     context = {
##         'category_list': get_category_cache()
##     }
##     return render(request, 'catalog/<name_page_for_categories>.html', context)



# Код на CBV для наглядности


class HomeListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/home.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(owner=self.request.user)

        return query


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):

        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')



