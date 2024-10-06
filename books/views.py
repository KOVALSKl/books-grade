import locale

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.shortcuts import get_object_or_404

from books.models import Book, BookFiltersForm
from books.utils import FiltersToKwargs

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy("books:index")


class BookListingView(TemplateView):
    template_name = 'books/book_listing.html'
    model = Book

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = BookFiltersForm(request.GET)

        context["filters_form"] = form

        if not form.is_valid():
            return self.render_to_response(context)

        with FiltersToKwargs(form.cleaned_data) as filters:
            books = self.get_queryset(**filters)

        context["books"] = books

        return self.render_to_response(context)

    def get_queryset(self, **kwargs):
        if bool(kwargs):
            return self.model.objects.filter(**kwargs)

        return self.model.objects.all()


class BookDetailView(TemplateView):
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        book_id = kwargs.get('id', None)
        book = get_object_or_404(self.model, pk=book_id)

        context['book'] = book
        context['created_at'] = book.created_at.strftime("%d %B %Y года")

        return context


