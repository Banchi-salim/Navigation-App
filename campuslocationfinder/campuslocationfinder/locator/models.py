from django.db import models


class UniAbujaCampus(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(max_length=100)
    campus = models.ForeignKey(UniAbujaCampus, on_delete=models.CASCADE)
    latitude = models.FloatField()  # Latitude of the building
    longitude = models.FloatField()  # Longitude of the building
    address = models.CharField(max_length=252)

    def __str__(self):
        return self.name
