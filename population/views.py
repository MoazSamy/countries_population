from .models import Population
from .serializers import PopulationSerializer
from rest_framework import generics
import requests
class PopulationList(generics.ListAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

def PopulationRetrieve(request):
    all_pops = {}
    url = "https://countriesnow.space/api/v0.1/countries/population"
    response = requests.get(url)
    data = response.json()
    countries = data['data']
    for i in countries:
        population_counts = i['populationCounts']
        for j in population_counts:
            country_attrs = {
                "country" : i['country'],
                "year" : j['year'],
                "pop" : j['value'],
            }
            Population.objects.create(**country_attrs)
    all_pops = Population.objects.all().order_by('country')
    
    return all_pops
