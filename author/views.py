from rest_framework import generics
from .serializers import AuthorDetailSerializer
from .serializers import AuthorListSerializer
from .models import Author


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorDetailSerializer


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorListSerializer
    queryset = Author.get_all()


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.get_all()