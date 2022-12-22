from django.urls import path
from .views import populationAPIView

urlpatterns = [path("", populationAPIView.as_view())]
