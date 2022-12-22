from django.urls import path
from .views import PopulationList,CountryDetailAPI
from .services import populate

urlpatterns = [path("", PopulationList.as_view()), path("populate/",populate), path("<str:code>/", CountryDetailAPI.as_view())]
