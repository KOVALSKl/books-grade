from django.contrib import admin
from .models import Book, Author, Genre


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    pass


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    pass
