from django.urls import path
from catalog.views import contacts, home, products
from  catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products')
]
