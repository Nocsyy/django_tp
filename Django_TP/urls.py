"""
URL configuration for Django_TP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import HttpResponse
from django.contrib.auth import views as auth_views

from TP.views.apiculteur import ApiculteurViewSet, ApiculteurListView
from TP.views.cheptel import CheptelViewSet, CheptelListView
from TP.views.contamination import ContaminationViewSet
from TP.views.interventions import InterventionViewSet
from TP.views.recolte import RecolteViewSet
from TP.views.ruche import RucheViewSet 
from TP.views.user import UserViewSet
from TP.views.home_page_view import ApiculteurCheptelListView

from TP.views.cheptel import CheptelListView

router = routers.DefaultRouter()
router.register(r'apiculteurs', ApiculteurViewSet)
router.register(r'cheptel', CheptelViewSet)
router.register(r'contamination', ContaminationViewSet)
router.register(r'intervention', InterventionViewSet)
router.register(r'recolte', RecolteViewSet)
router.register(r'ruche', RucheViewSet)
router.register(r'user', UserViewSet)

def home(request):
    return HttpResponse("Bienvenue sur l'API Apiculteur.")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('home/', CheptelListView.as_view()),
    path('apiculteurs/', ApiculteurCheptelListView.as_view(), name='home_page'),
    path('test_page/', CheptelViewSet.as_view({'get': 'list'}), name='home_page2')
    # ... (les autres URLs)
]