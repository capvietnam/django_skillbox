from rest_framework import serializers
from app_books.models import Books, Author


class BooksSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'author', 'title', 'isbn', 'description', 'date_release', 'pages']


class AuthorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'last_name', 'date_birthday']