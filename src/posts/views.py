from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm


class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bouton'] = 'Créer'
        context['title'] = 'Ajouter un article'
        return context


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    form_class = BlogPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bouton'] = 'Modifier'
        context['title'] = "Modifier l'article"
        return context


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = 'posts/show.html'
    context_object_name = 'post'


class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = 'posts/delete.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('posts:home')