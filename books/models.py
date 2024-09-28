from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    summary = models.TextField(null=True, blank=True)
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="authors")


class Genre(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="genres")

