from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from app_books.serializers import BooksSerializers, AuthorSerializers
from app_books.models import Books, Author


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    filterset_fields = ['author', 'title', 'pages']
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['pages']

    def get_queryset(self):
        books_pages = self.request.query_params.get('pages')
        if books_pages:
            self.queryset = self.queryset.filter(pages=books_pages)
        return self.queryset


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    filterset_fields = ['name']
