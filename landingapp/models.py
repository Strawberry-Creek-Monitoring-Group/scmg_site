from django.db import models

class NorthFork(models.Model):
    id = models.UUIDField(primary_key=True)
    timestamp = models.DateTimeField()
    conductivity = models.FloatField()
    depth = models.FloatField()
    temperature = models.FloatField()
    battery = models.FloatField()
    mayfly_temp = models.FloatField()
    signal_percent = models.FloatField()

    class Meta:
        db_table = 'north_fork'  # The name of the existing table in your database
        managed = False

    def __str__(self):
        return f"{self.timestamp}"