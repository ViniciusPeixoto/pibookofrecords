from django.urls import path

from book import views

urlpatterns = [
    path('users/', views.user_methods),
    path('users/<int:pk>', views.user_details),
    path('transactions/', views.transaction_methods),
    path('transactions/<int:pk>', views.transaction_details),
    path('sources/', views.source_methods),
    path('sources/<int:pk>', views.source_details),
]
