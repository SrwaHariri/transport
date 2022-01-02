from transportation_app.models import TransportItem, Category, Color
from transportation_app.api.serializers import TransportItemSerializer, CategorySerializer, ColorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets


class CategoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = ColorSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['name', ]


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    permission_classes = [AllowAny]


class TransportItem(viewsets.ModelViewSet):
    queryset = TransportItem.objects.all()
    serializer_class = TransportItemSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'colors', 'transport_model', ' category__name']
    ordering_fields = ['name']
    permission_classes = [IsAuthenticated]
