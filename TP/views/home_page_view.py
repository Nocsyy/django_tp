import django_filters
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers, permissions
from django.core.paginator import Paginator
from ..pagination import MyCustomPaginationClass
from ..models import Apiculteur, Cheptel, Ruche
from ..serializers import ApiculteurSerializer, CheptelSerializer, RucheSerializer


class ApiculteurCheptelListView(ListView):
    model = Apiculteur
    template_name = 'home_page.html'
    context_object_name = 'apiculteurs'
    paginate_by = 2  # Nombre d'apiculteurs par page

    def get_context_data(self, **kwargs):
        context = super(ApiculteurCheptelListView, self).get_context_data(**kwargs)
        context['cheptels'] = Cheptel.objects.all()  # Pas de pagination pour les cheptels
        return context

class ApiculteurFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter()
    prenom = django_filters.CharFilter()
    contact = django_filters.CharFilter()

    class Meta:
        model = Apiculteur
        fields = ['nom', 'prenom', 'contact']

class CheptelFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter()
    class Meta:
        model = Cheptel
        fields = ['nom']  # Remplacez par les champs réels de Cheptel

class RucheFilter(django_filters.FilterSet):
    statut = django_filters.ChoiceFilter(choices=Ruche.STATUT_CHOICES)
    type_abeille = django_filters.ChoiceFilter(choices=Ruche.TYPE_ABEILLE_CHOICES)

    class Meta:
        model = Ruche
        fields = ['statut', 'type_abeille']

class CheptelViewSet(viewsets.ModelViewSet):
    queryset = Cheptel.objects.all()
    serializer_class = ApiculteurSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ApiculteurFilter
    pagination_class = MyCustomPaginationClass

class CheptelViewSet(viewsets.ModelViewSet):
    queryset = Cheptel.objects.all()
    serializer_class = CheptelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CheptelFilter
    pagination_class = MyCustomPaginationClass
    
class RucheViewSet(viewsets.ModelViewSet):
    queryset = Ruche.objects.all()
    serializer_class = RucheSerializer  # Assurez-vous d'avoir un RucheSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = RucheFilter
    pagination_class = MyCustomPaginationClass