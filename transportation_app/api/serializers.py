from rest_framework import serializers, exceptions
from transportation_app.models import TransportItem, Category, Color


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')


class TransportItemSerializer(serializers.ModelSerializer):
    colors = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), many=True, required=False)

    class Meta:
        model = TransportItem
        fields = ('id', 'name', 'transport_model', 'category', 'colors')
        extra_kwargs = {
            'category': {
                'source': 'name'
            }
        }

    def validate_colors(self, value):
        if not len(value):
            raise exceptions.ValidationError('cannot be empty')
        return value


class ColorSerializer(serializers.ModelSerializer):
    transport_list = TransportItemSerializer(many=True, read_only=True)

    class Meta:
        model = Color
        fields = ('id', 'name', 'transport_list')
