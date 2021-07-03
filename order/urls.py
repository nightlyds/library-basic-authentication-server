from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderCreateList.as_view()),
    path('<int:pk>/', views.OrderRetrieveUpdateDelete.as_view())
]