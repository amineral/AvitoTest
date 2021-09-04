from rest_framework import serializers
from .models import Client, Operation, BankOperation

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"

class OperationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"

class BankOperationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankOperation
        fields = "__all__"
