from rest_framework import serializers
from .models import Reading

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ['id', 'sensor', 'timestamp', 'conductivity', 'depth', 'battery', 'mayfly_temp','signal_percent']