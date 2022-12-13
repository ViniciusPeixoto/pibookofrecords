from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book.models import Source, Transaction, User
from book.serializers import SourceSerializer, TransactionSerializer, UserSerializer
from book.utils import validate_signup, validate_source


@api_view(['GET', 'POST'])
def user_methods(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        validated_response = validate_signup(request.data)
        if validated_response:
            return validated_response

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):
    """
    Retrieve, update or delete a user
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def transaction_methods(request):
    """
    List all transactions, or create a new transaction.
    """
    if request.method == 'GET':
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def transaction_details(request, pk):
    """
    Retrieve, update or delete a transaction
    """
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def source_methods(request):
    """
    List all sources, or create a new source.
    """
    if request.method == 'GET':
        source = Source.objects.all()
        serializer = SourceSerializer(source, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        validated_response = validate_source(request.data)
        if validated_response:
            return validated_response

        serializer = SourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def source_details(request, pk):
    """
    Retrieve, update or delete a source
    """
    try:
        source = Source.objects.get(pk=pk)
    except Source.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SourceSerializer(source)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SourceSerializer(source, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        source.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
