from django.urls import path, include
from transportation_app.api.views import TransportItem, ColorViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('color', ColorViewSet, basename='color')
router.register('item', TransportItem, basename='item')

urlpatterns = [
    path('', include(router.urls)),
]
