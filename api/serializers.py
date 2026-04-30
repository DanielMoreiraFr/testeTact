from rest_framework import serializers
from data.models import DataModels

class DataModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModels
        fields = '__all__' # vai pegar todos as colunas do modelo que fiz no data models