from transportation_app.models import TransportItem, MainCategory, SubCategory, Color
from transportation_app.api.serializers import TransportItemSerializer, MainCategorySerializer, SubCategorySerializer, ColorSerializer
from rest_framework import  generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class MainCategoryList(generics.ListCreateAPIView):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class MainCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer


class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['parent', 'child_name']


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


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
