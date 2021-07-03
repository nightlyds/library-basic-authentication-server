from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView

urlpatterns = [
    path('create/', BookCreateView.as_view()),
    path('all/', BookListView.as_view()),
    path('detail/<int:pk>', BookDetailView.as_view()),
]
