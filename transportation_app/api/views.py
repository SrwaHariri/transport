from transportation_app.models import TransportItem, Category, Color
from transportation_app.api.serializers import TransportItemSerializer, CategorySerializer, ColorSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet


class CategoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = ColorSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
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
    permission_classes = [AllowAny]


class ColorDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [AllowAny]


class TransportItemList(generics.ListCreateAPIView):
    queryset = TransportItem.objects.all()
    serializer_class = TransportItemSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['name', 'colors', 'transport_model', ' category__name']
    ordering_fields = ['name']
    permission_classes = [IsAuthenticated]


class TransportItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransportItem.objects.all()
    serializer_class = TransportItemSerializer
    permission_classes = [IsAuthenticated]