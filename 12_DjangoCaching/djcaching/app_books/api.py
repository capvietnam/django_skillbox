from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from app_books.serializers import BooksSerializers, AuthorSerializers
from app_books.models import Books, Author
from django_filters.rest_framework import BaseInFilter, NumberFilter


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    in_stock = NumberFilter(field_name="quantity_remaining", lookup_expr="gt")
    filterset_fields = ['author', 'title', 'pages']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['pages']

    def get_queryset(self):
        books_pages = self.request.query_params.get('pages')
        books_pages1 = self.request.query_params.get('page>')
        books_pages2 = self.request.query_params.get('page<')
        if books_pages:
            self.queryset = self.queryset.filter(pages=books_pages)
        if books_pages1:
            self.queryset = self.queryset.filter(pages__gt=books_pages1)
        if books_pages2:
            self.queryset = self.queryset.filter(pages__lt=books_pages2)
        return self.queryset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    filterset_fields = ['name']
