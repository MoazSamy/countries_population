from .models import Population
from .serializers import PopulationSerializer
from rest_framework import generics

class PopulationList(generics.ListAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

class CountryDetailAPI(generics.ListAPIView):
    serializer_class = PopulationSerializer
    def get_queryset(self):
        return Population.objects.filter(code=self.kwargs['code'])