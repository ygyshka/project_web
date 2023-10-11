from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.views import (HomeListView, ProductDetailView, contacts,
                           ProductCreateView, ProductUpdateView, ProductDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(),  name='home'),
    path('contacts/', contacts, name='contacts'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    path('update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='update'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_confirm_delete'),
]
