from rest_framework import serializers
from book.models import User, Source, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'user_name',
            'user_email',
            'user_sources',
            'user_transactions'
            ]
        extra_kwargs = {
            'user_sources': {'required': False},
            'user_transactions': {'required': False}
        }

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_email = validated_data.get('user_email', instance.user_email)
        instance.user_sources = validated_data.get('user_sources', instance.sources)
        instance.user_transactions = validated_data.get('user_transactions', instance.user_transactions)
        instance.save()
        return instance


class SourceSerializer(serializers.ModelSerializer):
    source_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Source
        fields = [
            'id',
            'source_name',
            'source_users',
            'source_balance',
            'source_transactions',
            ]
        extra_kwargs = {
            'source_users': {'required': False},
            'source_transactions': {'required': False}
        }

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
        instance.source_transactions = validated_data.get('source_transactions', instance.source_transactions)
        instance.save()
        return instance


class TransactionSerializer(serializers.ModelSerializer):
    transaction_user = UserSerializer()
    transaction_source = SourceSerializer()

    class Meta:
        model = Transaction
        fields = [
            'id',
            'transaction_description',
            'transaction_date',
            'transaction_type',
            'transaction_user',
            'transaction_value',
            'transaction_source',
            ]
        extra_kwargs = {
            'transaction_user': {'required': False},
            'transaction_source': {'required': False}
        }

    def create(self, validated_data):
        """
        Create and return a new `Transaction` instance, given the validated data.
        """
        user_data = validated_data.pop('transaction_user')
        source_data = validated_data.pop('transaction_source')
        # this should be "get" because the system should not have duplicated users or sources
        user = User.objects.get(**user_data)
        source = Source.objects.get(**source_data)
        return Transaction.objects.create(transaction_user=user, transaction_source=source, **validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Transaction` instance, given the validated data.
        """
        instance.transaction_description = validated_data.get(
            'transaction_description', instance.transaction_description)
        instance.transaction_date = validated_data.get('transaction_date', instance.transaction_date)
        instance.transaction_type = validated_data.get('transaction_type', instance.transaction_type)
        instance.transaction_user = validated_data.get('transaction_user', instance.transaction_user)
        instance.transaction_value = validated_data.get('transaction_value', instance.transaction_value)
        instance.transaction_source = validated_data.get('transaction_source', instance.transaction_source)
        instance.save()
        return instance
