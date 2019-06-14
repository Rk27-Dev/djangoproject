from rest_framework import serializers
from .models import restmodel
class restserializer(serializers.Serializer):
    name =serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    sal = serializers.FloatField()
    ph_no = serializers.IntegerField()
    email = serializers.EmailField()