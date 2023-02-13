from rest_framework import routers
from app_books.api import BooksViewSet, AuthorViewSet
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register('books', BooksViewSet)
router.register('author', AuthorViewSet)

urlpatterns = router.urls + [
    path(r'books/<int:pk>', BooksDetail.as_view(), name=r'books-detail'),
    path(r'author/<int:pk>', AuthorDetail.as_view(), name=r'author-detail'),
]
