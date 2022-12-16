from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from book.views import UserViewSet, SourceViewSet, TransactionViewSet, api_root

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
user_details = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
source_list = SourceViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
source_details = SourceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
transaction_list = TransactionViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
transaction_details = TransactionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
transaction_show = TransactionViewSet.as_view({
    'get': 'show',
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = [
    path('', api_root),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>', user_details, name='user-details'),
    path('sources/', source_list, name='source-list'),
    path('sources/<int:pk>', source_details, name='source-details'),
    path('transactions/', transaction_list, name='transaction-list'),
    path('transactions/<int:pk>', transaction_details, name='transaction-details'),
    path('transactions/<int:pk>/data/', transaction_show, name='transaction-show')
]

urlpatterns = format_suffix_patterns(urlpatterns)
