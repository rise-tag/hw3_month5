from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.routers import DefaultRouter
from apps.books.views import BooksAPI

router = DefaultRouter()
router.register("api_books", BooksAPI, basename='api-books')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [

]

urlpatterns += router.urls
