from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView


class Index(View):
    def get(self, request):
        list_regions = ['Москва', 'Тула', 'Серпухов', 'США']
        return render(request, 'advertisements/index_list.html', {'list_regions': list_regions})


class Advertisements(View):
    def get(self, request):
        list_ads = ['машина', 'самокат', 'самолет', 'утюг']
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        return render(request, 'advertisements/advertisements-list.html', {'list_ads': list_ads,
                                                                          'num_visits': num_visits})

    def post(self, request):
        text = 'регион успешно создан'
        return render(request, 'advertisements/advertisements-list.html', {'text': text})


class My_contacts(TemplateView):
    template_name = 'advertisements/contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super(My_contacts, self).get_context_data(**kwargs)
        context['contexts'] = {'address': 'Moscow', 'number': '8 800 555-35-35', 'email': 'zenakorneev940@gmail.com'}
        return context


class About_google(TemplateView):
    template_name = 'advertisements/About.html'

    def get_context_data(self, **kwargs):
        context = super(About_google, self).get_context_data(**kwargs)
        context['name'], context['info'] = 'Google', 'Американская транснациональная корпорация'
        return context
