# models.py
from django.db import models

class Reading(models.Model):
    sensor = models.IntegerField()
    timestamp = models.TimeField()
    conductivity = models.FloatField()
    depth = models.FloatField()
    battery = models.FloatField()
    mayfly_temp = models.FloatField()
    signal_percent = models.FloatField()

    def __str__(self):
        return str(self.sensor) + str(self.timestamp)