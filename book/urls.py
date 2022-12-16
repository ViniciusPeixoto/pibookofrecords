from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'sources', views.SourceViewSet, basename='source')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls))
]
