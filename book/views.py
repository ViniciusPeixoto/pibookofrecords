from rest_framework import generics

from book.models import Source, Transaction, User
from book.serializers import SourceSerializer, TransactionSerializer, UserSerializer


class UserMethods(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SourceMethods(generics.ListCreateAPIView):
    """
    List all sources, or create a new source.
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetails(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update or delete a source
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class TransactionMethods(generics.ListCreateAPIView):
    """
    List all transactions, or create a new transaction.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetails(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update or delete a transaction
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
