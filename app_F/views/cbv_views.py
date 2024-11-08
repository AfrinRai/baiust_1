from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from ..models import Book
class BookListView(ListView):
    """
    View to display a list of all books.
    """
    model = Book
    template_name = 'books/book_list.html'  # Specify your template name
    context_object_name = 'books'  # Use this name in the template to access the list
    