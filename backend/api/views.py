from django.shortcuts import render
from .models import CSV
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CSVSerializer


class CSVViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CSV.objects.all()
    serializer_class = CSVSerializer
    permission_classes = [permissions.IsAuthenticated]

