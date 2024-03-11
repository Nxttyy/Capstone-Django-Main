from django.urls import path
from .views import home, book_detail, search_books

urlpatterns = [
    path('', home, name='book-home'),
    path('<int:book_id>/', book_detail, name='book-detail'),
    path('search/', search_books, name='search-results'),
    path('<int:book_id>/search/', search_books, name='search-results'),

]
