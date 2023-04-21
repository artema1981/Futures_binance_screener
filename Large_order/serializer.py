from rest_framework import serializers
from market_data.instans_lists import RenderDataBooks
#
class DepthBookSerializer(serializers.Serializer):
    get_unit_data = serializers.JSONField()