from django.db import models

class Client(models.Model):
    login = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.login

class Operation(models.Model):
    client_from = models.ForeignKey(Client, null=False, default=None, related_name="related_from", on_delete=models.CASCADE)
    client_to = models.ForeignKey(Client, null=False, default=None, related_name="related_to", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    currency = models.CharField(max_length=20, default="RUB")

class BankOperation(models.Model):
    client_to = models.ForeignKey(Client, null=False, default=None, on_delete=models.CASCADE)
    operation_type = models.CharField(max_length=4, null=False)
    value = models.IntegerField(default=0)

