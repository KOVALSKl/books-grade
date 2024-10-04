from django.db.models import DateTimeField
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404

from books.models import Book


class BookListingView(TemplateView):
    template_name = 'books/book_listing.html'
    model = Book

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        books = self.get_queryset()
        context = super().get_context_data(**kwargs)

        context['books'] = books
        context['authors'] = books.last().authors.all()

        return context



class BookDetailView(TemplateView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book_id = kwargs.get('id', None)
        book = get_object_or_404(self.model, pk=book_id)

        context['book'] = book
        context['date_time'] = book.created_at.to_python()

        return context


