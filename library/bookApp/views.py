from django.shortcuts import render
from django.http import HttpResponse
from bookApp.models import Comment, Book
from django.conf import settings
from bookApp.forms import CommentForm


# Create your views here.
def home(request):
	books = models.Book.objects.all()
	return render(request, 'bookApp/home.html', {'books':books, 'media_dir':settings.MEDIA_URL})


def book_detail(request, book_id):
	book = Book.objects.filter(id=book_id)
	comments = book.first().comment_set.all()

	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			cont = form.cleaned_data["content"]
			print(cont)
			_comment = Comment()
			_comment.content = form.cleaned_data["content"]
			_comment.book = book.first()
			_comment.save()
            # process the data in form.cleaned_data as required
            # ...
            # return HttpResponseRedirect("/thanks/")

	else:
		# comments = book.comment_set.all()
		form = CommentForm()

	return render(request, 'bookApp/book-detail.html', {'book':book, 'form':form, 'comments':comments})	# book_id = request.GET.get('book_id')
	
