
# Django imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError

# rest-framework imports
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# app imports
from .models import Client, Operation, BankOperation
from .serializers import (
    ClientSerializer, 
    ClientDetailSerializer, 
    OperationSerializer, 
    OperationDetailSerializer,
    BankOperationDetailSerializer,
)
from .exchange import exchange
from .errors import errors
from .config import EXCHANGE_IS_ACTIVE

# function as view
def api_help(request):
    return render(request, "avito_app/help.html")

@api_view(['POST'])
def add_client(request):  
    if request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse(errors["code_7"])
    else:
        return JsonResponse(errors["code_6"])

def depo_op(request):
    params = request.GET
    try: 
        if int(params["value"]) <= 0:
            return JsonResponse(errors["code_3"])
        value = int(params["value"])

        try:
            client = Client.objects.get(pk=int(params["id"]))
        except Client.DoesNotExist:
            return JsonResponse(errors["code_2"])
        
        client.balance += value
        client.save()

        bank_operation = BankOperation(client_to=client, operation_type="depo", value=value)
        bank_operation.save()
        serializer = BankOperationDetailSerializer(bank_operation)
        return JsonResponse(serializer.data)

    except MultiValueDictKeyError:
        return JsonResponse(errors["code_2"])


def draw_op(request):
    params = request.GET
    try:
        if int(params["value"]) <= 0:
            return JsonResponse(errors["code_3"])
        value = int(params["value"])

        try:
            client = Client.objects.get(pk=int(params["id"]))
        except Client.DoesNotExist:
            return JsonResponse(errors["code_2"])
        
        if client.balance < value:
            return JsonResponse(errors["code_5"])

        client.balance -= value
        client.save()

        bank_operation = BankOperation(client_to=client, operation_type="draw", value=value)
        bank_operation.save()
        serializer = BankOperationDetailSerializer(bank_operation)
        return JsonResponse(serializer.data)

    except MultiValueDictKeyError:
        return JsonResponse(errors["code_2"])


def transaction(request):
    """
        request params required:
            from : client.id
            to : client.id
            value : integer value
            currency : "RUB" default (OPTIONAL PARAM)
        
        return:
            ERROR: error details
            CONFIRMED: operation details as JSON view
    """
    params = request.GET
    try:
        try:
            from_id = Client.objects.get(id=int(params["from"])).id
            to_id = Client.objects.get(id=int(params["to"])).id
            client_from = Client.objects.get(id=from_id)
            client_to = Client.objects.get(id=to_id)
        except Client.DoesNotExist:
            return JsonResponse(errors["code_2"])

        if "currency" not in params or not EXCHANGE_IS_ACTIVE:
            currency = "RUB"
        else:
            currency = params["currency"]

        if "value" not in params:
            return JsonResponse(errors["code_3"])
        elif int(params["value"]) <= 0:
            return JsonResponse(errors["code_3"])

        value = int(params["value"])

        if currency != "RUB":
            to_rub = exchange(currency, value)
            value = to_rub
            if not value:
                return JsonResponse(errors["code_4"])
        
        description = f'From {client_from} {value} RUB to {client_to}'
        if client_from.balance < value:
            return JsonResponse(errors["code_5"])
        new_operation = Operation(
            client_from=client_from,
            client_to=client_to,
            description=description,
            value=value,
        )
        
        new_operation.currency = currency
        new_operation.save()
        client_from.balance -= value
        client_to.balance += value
        client_to.save()
        client_from.save()
        serializer = OperationDetailSerializer(new_operation)
        return JsonResponse(serializer.data)

    except MultiValueDictKeyError:
        return JsonResponse(errors["code_2"])
 
# class as view
class OperationListView(generics.ListAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

class OperationDetailView(generics.RetrieveAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationDetailSerializer

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailsView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
