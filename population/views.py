from .models import Population
from .serializers import PopulationSerializer
from rest_framework import generics

# Create your views here.


class populationAPIView(generics.ListAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

