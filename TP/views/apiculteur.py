import django_filters
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers, permissions
from django.shortcuts import render

from ..models import Apiculteur 
from ..serializers import ApiculteurSerializer

import logging

#logger = logging.getLogger(__name__)

class ApiculteurListView(ListView):
    model = Apiculteur
    template_name = 'home_page.html'


class ApiculteurFilter(django_filters.FilterSet):
    user = django_filters.CharFilter()
    class Meta:
        model = Apiculteur
        fields = {
            'user': ['exact'], 
        }

class ApiculteurViewSet(viewsets.ModelViewSet):
    queryset = Apiculteur.objects.all()
    serializer_class = ApiculteurSerializer
    filterset_class = ApiculteurFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]


