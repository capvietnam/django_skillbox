from django.shortcuts import render
from django.views.generic import View
from .models import Advertisements, Author, Category


class Advertisement(View):
    def get(self, request):
        advertisements = Advertisements.objects.all()
        author = Author.objects.all()
        category = Category.objects.all()
        title = 'Список объявлений'
        context = {
            'title': title,
            'author': author,
            'category': category,
            'advertisements': advertisements,
        }
        return render(request, 'advertisements_app/advertisements-list.html', context=context)


    def post(self, request):
        advertisements = Advertisements.objects.all()
        author = Author.objects.all()
        category = Category.objects.all()
        title = 'Список объявлений'
        context = {
            'title': title,
            'author': author,
            'category': category,
            'advertisements': advertisements,
        }
        return render(request, 'advertisements_app/advertisements-list.html', context=context)


def get_advertisement(request, id):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    advertisement_filter = Advertisements.objects.filter(pk=id)
    advertisements = Advertisements.objects.all()
    id = Advertisements.objects.get(pk=id)
    return render(request, 'advertisements_app/advertisement.html', {'advertisements': advertisements,
                                                                     'advertisement_filter': advertisement_filter,
                                                                     'id': id,
                                                                     'num_visits': num_visits,
                                                                     })
