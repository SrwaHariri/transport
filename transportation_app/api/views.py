from transportation_app.models import TransportItem, Category, Color
from transportation_app.api.serializers import TransportItemSerializer, CategorySerializer, ColorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['parent', 'child_name']


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ColorDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class TransportList(generics.ListCreateAPIView):
    queryset = TransportItem.objects.all()
    serializer_class = TransportItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'colors', 'transportModel', ' subCategory']


class TransportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransportItem.objects.all()
    serializer_class = TransportItemSerializer
