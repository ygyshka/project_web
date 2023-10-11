from django.urls import path
from django.views.decorators.cache import never_cache

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('view/<slug:slug>', never_cache(BlogDetailView.as_view()), name='view'),
    path('edit/<slug:slug>', never_cache(BlogUpdateView.as_view()), name='edit'),
    path('delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_confirm_delete'),
]
