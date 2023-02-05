from rest_framework import serializers
from .models import CSV
import hashlib

class CSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSV
        fields = '__all__'
    def create(self, validated_data):
        csv_file = validated_data.get('csv')
        validated_data['name'] = csv_file.name.split('.')[0]
        contents = csv_file.read()
        sha1 = hashlib.sha1(contents)
        validated_data['hash'] = sha1.hexdigest()
        return CSV.objects.create(**validated_data)
    


    