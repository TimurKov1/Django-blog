from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Record

class HomeShow(ListView):
    model = Record
    template_name = 'project/home.html'
    context_object_name = 'text'

    def get_context_data(self, **kwargs):
        context = super(HomeShow, self).get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

    def get_queryset(self):
        return Record.objects.order_by('-date')[:3]


class BlogShow(ListView):
    model = Record
    template_name = 'project/archive.html'
    context_object_name = 'text'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(BlogShow, self).get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self):
        return Record.objects.order_by('-date')

class DetailShow(DetailView):
    model = Record
    template_name = 'project/single.html'
    context_object_name = 'text'

    def get_context_data(self, **kwargs):
        context = super(DetailShow, self).get_context_data(**kwargs)
        context['title'] = 'Посты'
        return context