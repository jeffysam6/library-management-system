from django.shortcuts import render
from .models import Book,Author,BookInstance,Genre

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

def index(request):

	num_books = Book.objects.all().count()

	num_instances = BookInstance.objects.all().count()

	num_instances_available = BookInstance.objects.filter(status__exact='a').count()

	num_authors = Author.objects.all().count()

	num_humour = Book.objects.filter(genre__name__iexact='crime').count()


	context = {
	'num_books':num_books,
	'num_instances':num_instances,
	'num_instances_available':num_instances_available,
	'num_authors':num_authors,
	'num_humour':num_humour
	}

	return render(request,'catalog/index.html',context=context)



class BookListView(generic.ListView):
	model = Book



class BookDetailView(generic.DetailView):
	model = Book



class AuthorListView(generic.ListView):
	model = Author


class AuthorDetailView(generic.DetailView):
	model = Author