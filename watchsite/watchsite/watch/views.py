from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *
from .views import *



def index(request):
    return render(request, 'watch/index.html')


def about(request):
  return render(request, 'watch/about.html')


def contact(request):
    if request.method =="POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()
    return render(request, 'watch/contact.html', {'form': form})





class WatchHome(ListView):
    model = Watch
    template_name = 'watch/watches.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context



class WatchCategory(ListView):
    model = Watch
    template_name = 'watch/watches.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 1

    def get_queryset(self):
        return Watch.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['posts'][0].cat_id
        return context



class WatchesShow(DetailView):
    model = Watch
    template_name = 'watch/post_watch.html'
    context_object_name = 'posts'