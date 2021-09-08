from django.urls import path, include
from rest_framework import routers

from .views import (
    ClientListView, 
    ClientDetailsView, 
    OperationListView, transaction, 
    OperationDetailView,
    BankOperationListView,
    BankOperationDetailView,
    api_help,
    add_client,
    depo_op,
    draw_op,
    index_api,
)


urlpatterns = [
    path('', index_api, name="index_api"),
    path('help/', api_help, name='help'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailsView.as_view(), name="client_details"),
    path('transaq/', transaction, name='from_to_client_transaq'),
    path('operation/', OperationListView.as_view(), name='operation_list'),
    path('operation/<int:pk>', OperationDetailView.as_view(), name='operation_details'),
    path('depo/', depo_op, name='deposite'),
    path('draw/', draw_op, name='draw'),
    path('bankoper/', BankOperationListView.as_view(), name='bank_operation_list'),
    path('bankoper/<int:pk>', BankOperationDetailView.as_view(), name='bank_operation_detail'),
    path('client/new/', add_client, name='new_client'),
]