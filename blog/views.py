from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'to_published')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(to_published=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'to_published')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
            self.kwargs['slug'] = new_mat.slug
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('slug')])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
