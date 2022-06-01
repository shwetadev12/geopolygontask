from rest_framework import serializers
from mozio_app.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [
            'id',
            'name',
            'email',
            'phone_number',
            'language',
            'price',
            'price_currency'
        ]
        read_only_fields = ('id',)


class ServiceAreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceArea
        fields = [
            'id',
            'provider',
            'polygon',
            'polygon_name'
        ]
        read_only_fields = ('id',)


class GetPolygonsSerializer(serializers.ModelSerializer):
    provider = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ServiceArea
        fields = [
            'id',
            'provider',
            'polygon',
            'polygon_name'
        ]
        read_only_fields = ('id',)

    def get_provider(self, obj):
        return obj.provider.name
