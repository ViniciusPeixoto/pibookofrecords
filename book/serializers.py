from rest_framework import serializers
from book.models import User, Source, Transaction


class UserSerializer(serializers.ModelSerializer):
    user_transactions = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all(), required=False)
    user_sources = serializers.PrimaryKeyRelatedField(many=True, queryset=Source.objects.all(), required=False)

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
        # a new user must not have any sources nor transactions
        try:
            validated_data.pop('user_sources')
        except KeyError:
            pass
        try:
            validated_data.pop('user_transactions')
        except KeyError:
            pass
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
            'transaction_user': {'required': True},
            'transaction_source': {'required': True}
        }

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
        instance.transaction_user = validated_data.get('transaction_user', instance.transaction_user)
        instance.transaction_value = validated_data.get('transaction_value', instance.transaction_value)
        instance.transaction_source = validated_data.get('transaction_source', instance.transaction_source)
        instance.save()
        return instance
