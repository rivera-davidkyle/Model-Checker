from rest_framework import serializers
from .models import CSV
import hashlib
import pandas as pd
from io import StringIO

class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV
        fields = '__all__'
    def create(self, validated_data):
        csv_file = validated_data.get('csv')
        validated_data['name'] = csv_file.name.split('.')[0]
        contents = csv_file.read().decode('utf-8')
        sha1 = hashlib.sha1(contents.encode('utf-8'))
        validated_data['hash'] = sha1.hexdigest()
        df = pd.read_csv(StringIO(contents))
        validated_data['features'] = ",".join(df.columns)
        return CSV.objects.create(**validated_data)
    


    