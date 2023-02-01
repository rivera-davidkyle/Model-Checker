from rest_framework import serializers
from .models import CSV, PredModel



class CSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CSV
        fields = '__all__'


    