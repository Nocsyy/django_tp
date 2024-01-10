import django_filters
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers
from ..serializers import ContaminationSerializer
from ..models import Contamination

class ContaminationListView(ListView): 
    model = Contamination
    template_name = 'home_page.html'

class ContaminationFilter(django_filters.FilterSet):
    maladie = django_filters.ChoiceFilter(choices=Contamination.MALADIE_CHOICES)
    ruche = django_filters.CharFilter()
    class Meta:
        model = Contamination
        fields = {
            'maladie': ['exact', 'icontains'],
            'ruche': ['exact'],
           
            
        }

class ContaminationViewSet(viewsets.ModelViewSet): 
    queryset = Contamination.objects.all()
    serializer_class = ContaminationSerializer
    filterset_class = ContaminationFilter
    filter_backends = [DjangoFilterBackend]