import django_filters
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, serializers, permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.permissions import IsAuthenticated
from ..serializers import CheptelSerializer, RucheSerializer
from ..models import Cheptel, Ruche
from ..pagination import MyCustomPaginationClass

class CheptelListView(ListView):
    model = Cheptel
    queryset = Cheptel.objects.all()
    paginate_by = 2 
    def get_queryset(self):
        queryset = super().get_queryset()
        nom = self.request.GET.get('nom', None)

        if nom:
            queryset = queryset.filter(nom__exact=nom)

        return queryset

class CheptelFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter()
    class Meta:
        model = Cheptel
        fields = {
            'nom': ['exact'],
        }
class IsAuthenticatedOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Autoriser toutes les requêtes en lecture
        if request.method in SAFE_METHODS:
            return True

        # Vérifier si l'utilisateur est associé à un apiculteur
        user = request.user
        if hasattr(user, 'apiculteur'):
            # Récupérer les apiculteurs associés au cheptel
            keepers = obj.cheptel
            # Vérifier si l'apiculteur de l'utilisateur fait partie des apiculteurs du cheptel
            return user.apiculteur in keepers.all()
        
        return False

class CheptelViewSet(viewsets.ModelViewSet):
    queryset = Cheptel.objects.all()
    serializer_class= CheptelSerializer
    filterset_class = CheptelFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = MyCustomPaginationClass 
    template_name = 'home_page.html'

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

    
    







