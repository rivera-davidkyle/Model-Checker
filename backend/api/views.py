from django.shortcuts import render
from .models import CSV
from django.db import IntegrityError
from rest_framework import viewsets, permissions, status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CSVSerializer
import pandas as pd
import numpy as np
from .model_check import dtr_test, linear_test, svr_test

@api_view(['POST'])
def upload_csv(request):
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
@api_view(['GET'])
def get_model(request):
    if request.method == 'GET':
        csv = CSV.objects.get(hash=request.data['hash'])
        df = pd.read_csv(csv.file.path)
        df = df.drop(columns=request.data['drop'].split(","), axis=1)
        # Select columns with data type float64 or int64
        df = df.select_dtypes(include=["float64", "int64"])
        # Get the names of the remaining columns
        columns = df.columns
        # Drop all other columns
        df = df.drop([col for col in df.columns if col not in columns], axis=1)
        features = df.columns
        X = df.loc[:, features]
        y = df.loc[:, [request.data['target']]]
        reg_model = dtr_test(X, y)
        response_data = {
            "Model" : reg_model[0],
            "Score" : reg_model[1]
        }
        return Response(response_data)
        
        

