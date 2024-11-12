from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
# Create your views here.
from apps.books.models import Books
from apps.books.serializers import BooksSerializer

class Pagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10

class BooksAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = Pagination