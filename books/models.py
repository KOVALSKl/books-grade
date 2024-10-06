from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class Author(CreatedAtMixin):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __repr__(self):
        return f"Book({self.name}, {self.surname})"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Genre(CreatedAtMixin):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return f"Genre({self.name})"

    def __str__(self):
        return self.name


class Book(CreatedAtMixin):
    image = models.ImageField(
        verbose_name="Изображение",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    summary = models.TextField(
        null=True,
        blank=True,
        verbose_name="Краткое содержание",
    )
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рейтинг"
    )
    authors = models.ManyToManyField(
        Author,
        related_name="books",
        verbose_name="Авторы"
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="books",
        verbose_name="Жанры"
    )

    def __repr__(self):
        return f"Book({self.title}, {self.rating})"

    def __str__(self):
        return self.title


class BookFiltersForm(forms.Form):
    rating = forms.IntegerField(
        max_value=5,
        min_value=0,
        required=False,
        label="Рейтинг",
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        required=False,
        label="Авторы",
    )
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label="Жанры",
    )
