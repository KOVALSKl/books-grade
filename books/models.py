from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CreatedAtMixin:
    created_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model, CreatedAtMixin):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __repr__(self):
        return f"Book({self.name}, {self.surname})"

    def __str__(self):
        return f"{self.name} {self.surname}"


class Genre(models.Model, CreatedAtMixin):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return f"Genre({self.name})"

    def __str__(self):
        return self.name


class Book(models.Model, CreatedAtMixin):
    image = models.ImageField(
        null=True,
        blank=True,
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
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
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

