from rest_framework import serializers
from .models import Symbol, TopOfTheBook, Order

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = '__all__'

class TopOfTheBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopOfTheBook
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
