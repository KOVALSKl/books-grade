from django.urls import path

from .views import BookListingView, BookDetailView

urlpatterns = [
    path("", BookListingView.as_view() , name="index"),
    path("<int:id>", BookDetailView.as_view() , name="detail"),
]