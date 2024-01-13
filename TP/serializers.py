from rest_framework import serializers
from .models import Apiculteur, Cheptel, Ruche, Contamination, Intervention, Recolte, User

class ApiculteurSerializer(serializers.ModelSerializer):
    contact = serializers.CharField()
    class Meta:
        model = Apiculteur
        fields = '__all__'


class CheptelSerializer(serializers.ModelSerializer):
    apiculteur = ApiculteurSerializer(read_only=True)
    class Meta:
        model = Cheptel
        fields = '__all__'


class ContaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contamination
        fields = '__all__'


class InterventionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'

class RecolteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recolte
        fields = '__all__'

class RucheSerializer(serializers.ModelSerializer):
    cheptel = CheptelSerializer(read_only=True)
    class Meta:
        model = Ruche
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'nom', 'prenom', 'email']



