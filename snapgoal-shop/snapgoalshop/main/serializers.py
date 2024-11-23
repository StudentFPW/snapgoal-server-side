from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=False)
    uuid = serializers.UUIDField(required=False)
    price = serializers.IntegerField(required=True)
    image = serializers.URLField(required=True)
    category = serializers.CharField(max_length=255, required=False)
    availability = serializers.BooleanField(required=False)
    feedback = serializers.CharField(max_length=255, required=False)
