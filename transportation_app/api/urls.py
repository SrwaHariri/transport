from django.urls import path, include
from transportation_app.api.views import TransportItemList, TransportItemDetail, CategoryList, CategoryDetail, ColorList,\
    ColorDetail
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('item/', TransportItemList.as_view(), name='item-list'),
    path('item/<int:pk>', TransportItemDetail.as_view(), name='item-detail'),

    path('ctg/', CategoryList.as_view(), name='category'),
    path('ctg/<int:pk>', CategoryDetail.as_view(), name='category'),

    path('color/', ColorList.as_view(), name='color-list'),
    path('color/<int:pk>', ColorDetail.as_view(), name='color-detail'),

]
