from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthenticationListCreate.as_view()),
    path('login/', views.AuthenticationLogin.as_view()),
    path('<int:pk>/', views.AuthenticationRetrieveUpdateDestroy.as_view()),
]
