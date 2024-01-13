from django.views.generic import ListView, DetailView
from rest_framework import viewsets, serializers, permissions
from ..serializers import UserSerializer
from ..models import User
from ..pagination import MyCustomPaginationClass

class UserListView(ListView):
    model = User
    template_name = 'home_page.html'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = MyCustomPaginationClass 