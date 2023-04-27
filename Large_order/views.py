from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from market_data.instans_lists import *
from .serializer import DepthBookSerializer
from .utils import *
# Create your views here.

from .utils import *




class DepthBookAPIView(APIView):
    def get(self, request):
        GET = request.__dict__.get('_request').__dict__.get('GET')
        USDT_volume = GET.get('USDT_volume') if GET.get('USDT_volume') else 250000
        queryset = create_RDB_list(int(USDT_volume))
        output = DepthBookSerializer(queryset, many=True).data
        return Response(output)

