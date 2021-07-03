from rest_framework import generics
from .serializers import BookDetailSerializer
from .serializers import BookListSerializer
from .models import Book


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookDetailSerializer


class BookListView(generics.ListAPIView):
    serializer_class = BookListSerializer
    queryset = Book.get_all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookDetailSerializer
    queryset = Book.get_all()