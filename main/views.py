from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import DrugSerializer, DrugBatchSerializer, AlertSerializer
from .models import Drug, DrugBatch, Alert
from django.http import HttpResponse
from django.shortcuts import render

@api_view()
def drug_list(request):
    return Response('ok')

@api_view()
def drug_batch_list(request):
    return Response('ok')

@api_view()
def alert_list(request):
    return Response('ok')
