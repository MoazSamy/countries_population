from django.db import models

class Population(models.Model):
    country = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    pop = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.country
