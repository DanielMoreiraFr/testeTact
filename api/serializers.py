from rest_framework import serializers
from data.models import DataModels

class DataModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModels
        fields = '__all__' # pega todas as colunas do modelo DataModels da pasta data