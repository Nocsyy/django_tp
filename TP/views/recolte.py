from django.views.generic import ListView, DetailView
from rest_framework import viewsets, serializers
from ..serializers import RecolteSerializer
from ..models import Recolte

class RecolteListView(ListView):
    model = Recolte
    template_name = 'Recolte_list.html'

class RecolteViewSet(viewsets.ModelViewSet):
    queryset = Recolte.objects.all()
    serializer_class= RecolteSerializer