from django.shortcuts import render, redirect
from django.http import HttpResponse
from bookApp.models import Comment, Book
from django.conf import settings
from bookApp.forms import CommentForm, SearchForm, BookUploadForm, BookRatingForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q # new
# from users.views 

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

def book_rating(request, book_id):
	book = Book.objects.get(pk=book_id)

	if request.method == "POST":
		form = BookRatingForm(request.POST, instance=book)
		if form.is_valid():
			# print(request.FILES)
			book
			form.save()
			return redirect("/")
			
	else:
		if request.user in book.first().borrowers.all():
			is_user_borrower = True
		else:
			is_user_borrower = False
		context =  {'book':book, 'form':form, 'comments':comments, 'is_user_borrower':is_user_borrower}
		return render(request, 'bookApp/book_detail.html', context)	

def book_detail(request, book_id):
	book = Book.objects.filter(id=book_id)
	comments = book.first().comment_set.all()

	
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			_comment = Comment()
			_comment.content = form.cleaned_data["content"]
			_comment.book = book.first()
			_comment.poster = request.user
			_comment.save()

	
	if request.user in book.first().borrowers.all():
		is_user_borrower = True
	else:
		is_user_borrower = False

	context =  {'book':book, 'comment_form':CommentForm(), 'rating_form':BookRatingForm(), 'comments':comments, 'is_user_borrower':is_user_borrower}

	return render(request, 'bookApp/book_detail.html', context)	
	
class SearchResultsView(ListView):
	model = Book
	template_name = "bookApp/search.html"
	context_object_name = 'books'


	def get_queryset(self):  # new
		query = self.request.GET.get("q")
		object_list = Book.objects.filter(
			Q(title__icontains=query) | Q(author__icontains=query)
		)
		return object_list

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
			rating = form.cleaned_data['rating']
			# bad ratting calculation (needs improvement)
			book.rating = (book.rating + rating)/2
			book.save()
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
		messages.error(request, "Privilaged Action For Admin and SuperAdmin Only!")
		return redirect("book-detail")
	return redirect('book-home')	


@login_required
def borrow(request, book_id):
	user = request.user
	book = Book.objects.get(pk=book_id)


	if len(user.book_set.all()) >= 3:
		if book.pcs_left <= 0:
			messages.error(request, f"All the copies are taken, visit later!")
			return redirect('book-home')

		messages.error(request, f"You have reached the limit for borrowing books, return some to borrow again.")
		return redirect('user-account')
	else:
		book.pcs_left = book.pcs_left - 1
		book.borrowers.add(user)
		book.save()

		messages.success(request, f"You succesfuly borrowed, {book.title}")
		return redirect('user-account')

@login_required
def return_book(request, book_id):
	user = request.user
	book = Book.objects.get(pk=book_id)
	book.borrowers.remove(user)
	book.pcs_left = book.pcs_left + 1
	book.save()

	messages.success(request, f"You succesfuly retuned, {book.title}")
	return redirect('user-account')