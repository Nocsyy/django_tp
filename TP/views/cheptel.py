import django_filters
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated
from ..serializers import CheptelSerializer, RucheSerializer
from ..models import Cheptel, Ruche

class CheptelListView(ListView):
    model = Cheptel
    template_name = 'home_page.html'
    queryset = Cheptel.objects.all()

class InterventionFilter(django_filters.FilterSet):
   
    nom = django_filters.CharFilter()
    class Meta:
        model = Cheptel
        fields = {
            'nom': ['exact'],
           
            
        }

class CheptelViewSet(viewsets.ModelViewSet):
    queryset = Cheptel.objects.all()
    serializer_class= CheptelSerializer
    filterset_class = InterventionFilter
    filter_backends = [DjangoFilterBackend]

    @action(detail=True, methods=['put'])
    def mettre_a_jour_statut_ruches(self, request, pk=None):
        cheptel = self.get_object()
        nouvelles_donnees = request.data

        ruches_du_cheptel = Ruche.objects.filter(cheptel=cheptel)
        ruches_du_cheptel.update(statut=nouvelles_donnees.get('nouveau_statut'))

        serializer = RucheSerializer(ruches_du_cheptel, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['put'])
    def mettre_a_jour_la_contamination(self, request, pk=None):
        cheptel = self.get_object()
        nouvelles_donnees = request.data

        ruches_du_cheptel = Ruche.objects.filter(cheptel=cheptel)
        ruches_du_cheptel.update(contamination=nouvelles_donnees.get('nouveau_statut_contamination'))

        serializer = RucheSerializer(ruches_du_cheptel, many=True)
        return Response(serializer.data)

    
    
