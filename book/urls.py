from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from book import views

urlpatterns = [
    path('users/', views.UserMethods.as_view()),
    path('users/<int:pk>', views.UserDetails.as_view()),
    path('sources/', views.SourceMethods.as_view()),
    path('sources/<int:pk>', views.SourceDetails.as_view()),
    path('transactions/', views.TransactionMethods.as_view()),
    path('transactions/<int:pk>', views.TransactionDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
