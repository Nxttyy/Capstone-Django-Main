from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.conf import settings


# Create your views here.
def home(request):
	books = models.Book.objects.all()
	print(books)
	return render(request, 'bookApp/home.html', {'books':books, 'media_dir':settings.MEDIA_URL})


def book_detail(request, book_id):
	# book_id = request.GET.get('book_id')
	book = models.Book.objects.filter(id=book_id)
	print(book)
	return render(request, 'bookApp/book-detail.html', {'book':book})