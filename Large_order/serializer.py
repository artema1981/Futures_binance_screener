from rest_framework import serializers


class DepthBookSerializer(serializers.Serializer):
    get_unit_data = serializers.JSONField()
