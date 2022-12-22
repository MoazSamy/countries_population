from rest_framework import serializers
from .models import Population


class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = {"country", "year", "population"}
