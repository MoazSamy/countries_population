from .models import Population
from .serializers import PopulationSerializer
from rest_framework import generics
from django.http import Http404


class PopulationList(generics.ListAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer


class CountryDetailAPI(generics.ListAPIView):
    serializer_class = PopulationSerializer

    def get_queryset(self):
        populations = Population.objects.filter(code=self.kwargs["code"])
        if not populations:
            raise Http404
        else:
            return populations
