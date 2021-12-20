from transportation_app.models import TransportItem, Category, Color
from transportation_app.api.serializers import TransportItemSerializer, CategorySerializer, ColorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['name', ]

    def post(self, request, *args, **kwargs):
        print(request.user)
        return super().post(request, *args, **kwargs)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ColorDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TransportItemList(generics.ListCreateAPIView):
    queryset = TransportItem.objects.all()
    serializer_class = TransportItemSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'colors', 'transport_model', ' category__name']
    ordering_fields = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class TransportItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransportItem.objects.all()
    serializer_class = TransportItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]