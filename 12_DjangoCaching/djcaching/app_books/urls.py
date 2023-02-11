from rest_framework import routers
from app_books.api import BooksViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register('books', BooksViewSet)
router.register('author', AuthorViewSet)
urlpatterns = router.urls
