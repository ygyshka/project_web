from django.urls import path
from catalog.views import (HomeListView, ProductDetailView, contacts,
                           ProductCreateView, ProductUpdateView, ProductDeleteView) #home_list_view,
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(),  name='home'),
    path('contacts/', contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_confirm_delete'),
]
