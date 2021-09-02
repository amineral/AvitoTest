
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
from .models import Client, Operation
from .serializers import (
    ClientSerializer, 
    ClientDetailSerializer, 
    OperationSerializer, 
    OperationDetailSerializer,
)
from .exchange import exchange

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
            return render(request, "avito_app/error.html", {"error_code" : 2})

        if "currency" not in params:
            currency = "RUB"
        else:
            currency = params["currency"]
        if "value" not in params:
             return render(request, "avito_app/error.html", {"error_code" : 3})
        elif int(params["value"]) <= 0:
             return render(request, "avito_app/error.html", {"error_code" : 3})

        value = int(params["value"])
        if "currency" != "RUB":
            to_rub = exchange(currency, value)
            value = to_rub
            if not value:
                return render(request, "avito_app/error.html", {"error_code" : 4})
        description = f'From {client_from} {value} {currency} to {client_to}'
        if client_from.balance < value:
            return HttpResponse("There is not enough on balance")
        new_operation = Operation(
            client_from=client_from,
            client_to=client_to,
            description=description,
            value=value,
        )
        
        new_operation.save()
        client_from.balance -= value
        client_to.balance += value
        client_to.save()
        client_from.save()
        serializer = OperationDetailSerializer(new_operation)

        return JsonResponse(serializer.data)

    except MultiValueDictKeyError:
        return render(request, "avito_app/error.html", {"error_code" : 1})
 
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
