from django.urls import path, include
from rest_framework import routers

from .views import (
    ClientListView, 
    ClientDetailsView, 
    OperationListView, transaction, 
    OperationDetailView,
    api_help,
    add_client,
    depo_op,
    draw_op,
)

urlpatterns = [
    path('help/', api_help, name='help'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailsView.as_view()),
    path('operation/', OperationListView.as_view()),
    path('operation/<int:pk>', OperationDetailView.as_view(), name='operation_details'),
    path('transaq/', transaction),
    path('client/new/', add_client),
    path('depo/', depo_op),
    path('draw/', draw_op),
]