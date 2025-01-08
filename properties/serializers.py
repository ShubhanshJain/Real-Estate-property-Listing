from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['property_id', 'user', 'created_at', 'status']

class PropertyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['location', 'price', 'property_type', 'description', 'amenities']
