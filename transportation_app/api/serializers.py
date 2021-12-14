from rest_framework import serializers
from transportation_app.models import TransportItem, MainCategory, SubCategory, Color


class MainCategorySerializer(serializers.HyperlinkedModelSerializer):

    parent_id = serializers.PrimaryKeyRelatedField(queryset=MainCategory.objects.all(), source='parent.id')

    class Meta:
        model = SubCategory
        fields = ('child_name', 'parent_id')

    def create(self, validated_data):
        subject = SubCategory.objects.create(parent=validated_data['parent']['id'], child_name=validated_data['SubCategory'])

        return SubCategory


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    children = MainCategorySerializer(many=True, read_only=True)

    class Meta:
        model = MainCategory
        fields = ('name', 'children')


class TransportItemSerializer(serializers.ModelSerializer):
    colors = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), many=True)

    class Meta:
        model = TransportItem
        fields = ('name', 'transportModel', 'subCategory', 'colors')


class ColorSerializer(serializers.ModelSerializer):
    transport_list = TransportItemSerializer(many=True, read_only=True)

    class Meta:
        model = Color
        fields = ('name', 'transport_list')


