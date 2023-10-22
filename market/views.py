from rest_framework import viewsets
from .models import Symbol, TopOfTheBook, Order
from .serializers import SymbolSerializer, TopOfTheBookSerializer, OrderSerializer

class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer

class TopOfTheBookViewSet(viewsets.ModelViewSet):  # Make sure this class is named correctly
    queryset = TopOfTheBook.objects.all()
    serializer_class = TopOfTheBookSerializer

class OrderViewSet(viewsets.ModelViewSet):  # Make sure this class is named correctly
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
