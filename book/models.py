from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    user_email = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.user_name


class Source(models.Model):
    source_name = models.CharField(max_length=50, unique=True)
    source_balance = models.IntegerField(default=0)

    source_users = models.ManyToManyField('User', related_name='user_sources', blank=True)

    def __str__(self):
        return self.source_name


class Transaction(models.Model):
    transaction_description = models.CharField(max_length=50, null=True)
    transaction_value = models.IntegerField(default=0)
    transaction_date = models.DateTimeField('transaction date')
    transaction_type = models.CharField(max_length=50)

    transaction_source = models.ForeignKey('Source', related_name='source_transactions', on_delete=models.CASCADE)
    transaction_user = models.ForeignKey('User', related_name='user_transactions', on_delete=models.CASCADE)

    def __str__(self):
        return self.transaction_description

    class Meta:
        ordering = ['transaction_date']
