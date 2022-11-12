from django.urls import path

from book import views

urlpatterns = [
    path('users/', views.user_methods),
]
