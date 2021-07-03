from django.urls import path
from .views import *

urlpatterns = [
    path('create/', AuthorCreateView.as_view()),
    path('all/', AuthorListView.as_view()),
    path('detail/<int:pk>', AuthorDetailView.as_view()),
]
