from django.urls import path, include
from transportation_app.api.views import TransportItemList, TransportItemDetail, CategoryList, CategoryDetail, ColorList,\
    ColorDetail, CategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [

    path('', include(router.urls)),
    path('item/', TransportItemList.as_view(), name='item-list'),
    path('item/<int:pk>', TransportItemDetail.as_view(), name='item-detail'),

    path('ctg/', CategoryList.as_view(), name='category-list'),
    path('ctg/<int:pk>', CategoryDetail.as_view(), name='category-detail'),

    path('color/', ColorList.as_view(), name='color-list'),
    path('color/<int:pk>', ColorDetail.as_view(), name='color-detail'),

]
