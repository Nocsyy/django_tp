import django_filters
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers, permissions
from django_filters import rest_framework as filters
from ..serializers import RucheSerializer
from ..models import Ruche


class RucheListView(ListView):
    model = Ruche
    template_name = 'home_page.html'

class RucheFilter(django_filters.FilterSet):
    statut = django_filters.ChoiceFilter(choices=Ruche.STATUT_CHOICES)
    type_abeille = django_filters.ChoiceFilter(choices=Ruche.TYPE_ABEILLE_CHOICES)
    contamination = django_filters.BooleanFilter()
    class Meta:
        model = Ruche
        fields = {
            'type_abeille': ['exact', 'icontains'],
            'statut': ['exact', 'icontains'],
            'contamination': ['exact'],
            
        }

class RucheViewSet(viewsets.ModelViewSet):
    queryset = Ruche.objects.all()
    serializer_class= RucheSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RucheFilter
    permission_classes = [permissions.IsAuthenticated]

    
