from django.shortcuts import render
from .models import CSV
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import views, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CSVSerializer


@api_view(['POST'])
def csv_upload(request):
    if request.method == 'POST':
        serializer = CSVSerializer(data=request.data)
        if serializer.is_valid():
            csv = serializer.save()
            csv.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

