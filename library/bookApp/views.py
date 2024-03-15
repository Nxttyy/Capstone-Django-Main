from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookApp.models import Comment, Book
from django.conf import settings
from bookApp.forms import CommentForm, SearchForm, BookUploadForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.contrib import messages


class BookListView(ListView):
	model = Book
	template_name = 'bookApp/home.html'
	context_object_name = 'books'
	ordering = ['-created_at']
	paginate_by = 2



	def get_context_data(self, **kwargs):
		context = super(BookListView, self).get_context_data(**kwargs)
		user = self.request.user
		if user:
			context['user'] = user
		return context

@login_required
def book_upload(request):
	if request.method == "POST":
		form = BookUploadForm(request.POST, request.FILES)
		if form.is_valid():
			print(request.FILES)
			form.save()
			return redirect("/")
			
	else:
		form = BookUploadForm()
	return render(request, 'bookApp/book_upload.html', {'form':form})


def book_detail(request, book_id):
	book = Book.objects.filter(id=book_id)
	comments = book.first().comment_set.all()

	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
		    # comment = form.save(commit=False)
		    # profile.poster = request.user
		    # profile.save()

			_comment = Comment()
			_comment.content = form.cleaned_data["content"]
			_comment.book = book.first()
			_comment.poster = request.user
			_comment.save()

	else:
		form = CommentForm()

	return render(request, 'bookApp/book_detail.html', {'book':book, 'form':form, 'comments':comments, 'search_form':SearchForm()})	# book_id = request.GET.get('book_id')
	

def search_books(request, book_id=None):
	# form = SearchForm()
	books = []
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			prompt = form.cleaned_data["prompt"]
			books = help_search(prompt)
			
	else:
		form = CommentForm()
	return render(request, 'bookApp/search.html', {'search_form':form, 'book':books})

def help_search(prompt):
	by_title = Book.objects.filter(title=prompt)
	by_author = Book.objects.filter(author=prompt)
	return by_title + by_author

@login_required
def edit_book(request, book_id):
	book = Book.objects.get(pk=book_id)

	if request.method == "POST":
		form = BookUploadForm(request.POST, request.FILES, instance=book)
		if form.is_valid():
			print(request.FILES)
			form.save()
			return redirect("/")
			
	else:
		form = BookUploadForm(instance=book)
	return render(request, 'bookApp/book_upload.html', {'form':form})

@login_required
def delete_book(request, book_id):
	user = request.user
	if user.is_staff or user.role == 'Admin':
		try:
			book = Book.objects.get(pk=book_id)
		except Book.DoesNotExist:
			book = None
		if book:
			book.delete()
			messages.success(request, "Book Deleted!")
			return redirect("book-detail")
	else:
		messages.alert(request, "Privilaged Action For Admin and SuperAdmin Only!")
		return redirect("book-detail")
	return redirect('book-home')	


@login_required
def borrow(request, book_id):
	print("borrowed")
	user = request.user
	book = Book.objects.get(pk=book_id)
	book.borrowers.add(user)
	book.save()

	return redirect('book-home')