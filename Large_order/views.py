from django.shortcuts import render
from rest_framework import generics
from market_data.instans_lists import *
from .serializer import DepthBookSerializer
from .utils import *
# Create your views here.

from .utils import *

class DepthBookAPIView(generics.ListAPIView):

    # create_RDB_list(250000)
    # print('view', RDB_list)
    queryset = create_RDB_list(10)
    serializer_class = DepthBookSerializer



