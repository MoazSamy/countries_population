from django.urls import path
from .views import PopulationList,PopulationRetrieve

urlpatterns = [path("", PopulationList.as_view()), path("retrieve/",PopulationRetrieve)]
