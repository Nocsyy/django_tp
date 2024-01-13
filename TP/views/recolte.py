from django.views.generic import ListView, DetailView
from rest_framework import viewsets, serializers, permissions
from ..serializers import RecolteSerializer
from ..models import Recolte

class RecolteListView(ListView):
    model = Recolte
    template_name = 'home_page.html'

class RecolteViewSet(viewsets.ModelViewSet):
    queryset = Recolte.objects.all()
    serializer_class= RecolteSerializer
    permission_classes = [permissions.IsAuthenticated]