from rest_framework import renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from book.models import Source, Transaction, User
from book.serializers import SourceSerializer, TransactionSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    List and retrieves users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SourceViewSet(viewsets.ModelViewSet):
    """
    List and retrieves sources
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    List, retrieves and displays transactions
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def show(self, request, *args, **kwargs):
        transaction = self.get_object()
        return Response(transaction.transaction_description)

    def perform_create(self, serializer):
        serializer.save()


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "users": reverse('user-list', request=request, format=format),
        "sources": reverse('source-list', request=request, format=format),
        "transactions": reverse('transaction-list', request=request, format=format)
    })
