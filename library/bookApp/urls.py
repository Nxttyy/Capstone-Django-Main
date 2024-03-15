from django.urls import path
from .views import (book_detail, 
    SearchResultsView, 
    book_upload, 
    BookListView, 
    borrow, 
    delete_book, 
    edit_book, 
    return_book,
    book_rating)

urlpatterns = [
    path('', BookListView.as_view(), name='book-home'),
    # path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:book_id>/', book_detail, name='book-detail'),
    path('book/upload/', book_upload, name='book_upload'),
    path('book/search/', SearchResultsView.as_view(), name='search-results'),
    path('book/borrow/<int:book_id>/', borrow, name='book-borrow'),
    path('book/return/<int:book_id>/', return_book, name='book-return'),
    path('book/rate/<int:book_id>/', book_rating, name='book-rate'),

    path('book/delete_book/<int:book_id>/', delete_book, name='book-delete'),
    path('book/edit_book/<int:book_id>/', edit_book, name='book-edit'),


    # path('<int:book_id>/search/', search_books, name='search-results'),

]
