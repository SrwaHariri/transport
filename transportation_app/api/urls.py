from django.urls import path, include
from transportation_app.api.views import TransportList, TransportDetail, CategoryList, CategoryDetail, ColorList,\
    ColorDetail
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('item/', TransportList.as_view(), name='transport-list'),
    path('item/<int:pk>', TransportDetail.as_view(), name='transport-detail'),

    path('ctg/', CategoryList.as_view(), name='category'),
    path('ctg/<int:pk>', CategoryDetail.as_view(), name='category'),

    path('color/', ColorList.as_view(), name='color-list'),
    path('color/<int:pk>', ColorDetail.as_view(), name='color-detail'),

]
