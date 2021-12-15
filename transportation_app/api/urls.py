from django.urls import path, include
from transportation_app.api.views import TransportList, TransportDetail, MainCategoryList, MainCategoryDetail, SubCategoryList, SubCategoryDetail, ColorList, ColorDetail
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('item/', TransportList.as_view(), name='transport-list'),
    path('item/<int:pk>', TransportDetail.as_view(), name='transport-detail'),

    path('main/', MainCategoryList.as_view(), name='main-category'),
    path('main/<int:pk>', MainCategoryDetail.as_view(), name='main-category'),

    path('sub/', SubCategoryList.as_view(), name='main-category'),
    path('subc/<int:pk>', SubCategoryDetail.as_view(), name='main-category'),

    path('color/', ColorList.as_view(), name='color-list'),
    path('color/<int:pk>', ColorDetail.as_view(), name='color-detail'),

]
