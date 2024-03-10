from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.conf import settings


# Create your views here.
def home(request):
	books = models.Book.objects.all()
	print(books)
	return render(request, 'bookApp/home.html', {'books':books, 'media_dir':settings.MEDIA_URL})