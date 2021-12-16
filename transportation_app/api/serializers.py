from rest_framework import serializers
from transportation_app.models import TransportItem, Category, Color


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class TransportItemSerializer(serializers.ModelSerializer):
    colors = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), many=True)

    class Meta:
        model = TransportItem
        fields = ('name', 'transport_model', 'category', 'colors')


class ColorSerializer(serializers.ModelSerializer):
    transport_list = TransportItemSerializer(many=True, read_only=True)

    class Meta:
        model = Color
        fields = ('name', 'transport_list')
