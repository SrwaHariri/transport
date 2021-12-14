from transportation_app.models import TransportItem, MainCategory, SubCategory, Color
from transportation_app.api.serializers import TransportItemSerializer, MainCategorySerializer, SubCategorySerializer, ColorSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class TransportList(APIView):
    def get(self, request):
        transportitem = TransportItem.objects.all()
        serializer = TransportItemSerializer(
            transportitem, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TransportItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TransportDetail(APIView):

    def get(self, request, pk):
        try:
            transportitem = TransportItem.objects.get(pk=pk)
        except TransportItem.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransportItemSerializer(
            transportitem, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        transportitem = TransportItem.objects.get(pk=pk)
        serializer = TransportItemSerializer(transportitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transportitem= TransportItem.objects.get(pk=pk)
        transportitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MainCategoryList(APIView):

    def get(self, request):
        maincategory = MainCategory.objects.all()
        serializer = MainCategorySerializer(
            maincategory, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MainCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MainCategoryDetail(APIView):

    def get(self, request, pk):
        try:
            maincategory= MainCategory.objects.get(pk=pk)
        except MainCategory.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MainCategorySerializer(
            maincategory, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        maincategory = MainCategory.objects.get(pk=pk)
        serializer = MainCategorySerializer(maincategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        maincategory= MainCategory.objects.get(pk=pk)
        maincategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubCategoryList(APIView):

    def get(self, request):
        subcategory = SubCategory.objects.all()
        serializer = SubCategorySerializer(
            subcategory, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class SubCategoryDetail(APIView):

    def get(self, request, pk):
        try:
            subcategory= SubCategory.objects.get(pk=pk)
        except SubCategory.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubCategorySerializer(
            subcategory, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        subcategory = SubCategory.objects.get(pk=pk)
        serializer = SubCategorySerializer(subcategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subcategory= SubCategory.objects.get(pk=pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ColorList(APIView):

    def get(self, request):
        color = Color.objects.all()
        serializer = ColorSerializer(
            color, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ColorDetail (APIView):

    def get(self, request, pk):
        try:
            color = Color.objects.get(pk=pk)
        except Color.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ColorSerializer(
           color, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        color = Color.objects.get(pk=pk)
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        color= Color.objects.get(pk=pk)
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)