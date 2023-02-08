from django.shortcuts import render
from .models import CSV
from django.db import IntegrityError
from rest_framework import viewsets, permissions, status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CSVSerializer
import pandas as pd


@api_view(['POST'])
def csv_upload(request):
    if request.method == 'POST':
        serializer = CSVSerializer(data=request.data)
        if serializer.is_valid():
            try:
                csv = serializer.save()
                csv.save()
                features = csv.features.split(",")
                response_data = {
                    'serializer_data': serializer.data,
                    'features': features
                }
            except IntegrityError as e:
                return Response({'error': 'Integrity error: {}'.format(e)},
                        status=status.HTTP_400_BAD_REQUEST)
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

