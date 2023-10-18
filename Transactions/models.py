from django.db import models
from Users.models import CustomUser


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('deposit', 'Deposit'),
    ]

    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()}: {self.amount} to {self.account.phone_number}"