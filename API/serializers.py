from dataclasses import fields
from xml.parsers.expat import model
from rest_framework.serializers import ModelSerializer

from API.models import Pet, Product

class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'