from rest_framework import serializers
from book.models import User, Source, Transaction


class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = (
            'id',
            'transaction_description',
            'transaction_value',
            'transaction_date',
            'transaction_type',
            'transaction_source'
            )
        extra_kwargs = {'transaction_source': {'required': False}}

    def create(self, validated_data):
        """
        Create and return a new `Transaction` instance, given the validated data.
        """
        return Transaction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Transaction` instance, given the validated data.
        """
        instance.transaction_description = validated_data.get(
            'transaction_description', instance.transaction_description)
        instance.transaction_date = validated_data.get('transaction_date', instance.transaction_date)
        instance.transaction_type = validated_data.get('transaction_type', instance.transaction_type)
        instance.transaction_value = validated_data.get('transaction_value', instance.transaction_value)
        instance.transaction_source = validated_data.get('transaction_source', instance.transaction_source)
        instance.save()
        return instance


class SourceSerializer(serializers.Serializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = Source
        fields = (
            'id',
            'source_name',
            'source_balance',
            'source_users',
            'transactions'
            )
        extra_kwargs = {'source_users': {'required': False}}

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Source.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.source_name = validated_data.get('source_name', instance.source_name)
        instance.source_users = validated_data.get('source_users', instance.source_users)
        instance.source_balance = validated_data.get('source_balance', instance.source_balance)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    sources = SourceSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'user_name',
            'user_email',
            'sources'
            )
        extra_kwargs = {'sources': {'required': False}}

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.sources = validated_data.get('sources', instance.sources)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.save()
        return instance
