
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Advertisements, Author, Category

class Advertisement(ListView):
    model = Advertisements
    template_name = 'advertisements_app/advertisements-list.html'
    context_object_name = 'Advertisements'
    extra_context = {'title': 'Список объявлений'}


class Get_advertisement(DetailView):

    model = Advertisements
    context_object_name = 'Advertisement'
    template_name = 'advertisements_app/advertisement-detail.html'
    model.views_count = 0


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Get_advertisement, self).get_context_data(**kwargs)
        context['title'] = Advertisements.objects.get(pk=self.kwargs['pk'])
        context['obj'] = self.model.views_count
        return context


    def get_object(self, queryset=None):
        obj = super(Get_advertisement, self).get_object(queryset=queryset)
        self.model.views_count += 1
        return obj

    def get_queryset(self):
        return Advertisements.objects.filter(pk=self.kwargs['pk'])
