import django_filters
from django.views.generic import ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, serializers, permissions
from ..serializers import InterventionsSerializer
from ..models import Intervention
from ..pagination import MyCustomPaginationClass

class InterventionListView(ListView):
    model = Intervention
    template_name = 'home_page.html'


class InterventionFilter(django_filters.FilterSet):
    nature = django_filters.ChoiceFilter(choices=Intervention.NATURE_CHOICES)
    ruche = django_filters.CharFilter()
    class Meta:
        model = Intervention
        fields = {
            'nature': ['exact', 'icontains'],
            'ruche': ['exact'],
           
            
        }

class InterventionViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class= InterventionsSerializer
    filterset_class = InterventionFilter
    filter_backends = [DjangoFilterBackend]
    pagination_class = MyCustomPaginationClass 
    permission_classes = [permissions.IsAuthenticated]
