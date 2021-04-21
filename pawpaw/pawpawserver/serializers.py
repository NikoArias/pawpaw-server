from rest_framework import serializers
from pawpawserver.models import TimeSeriesDatum, Instrument


class TimeSeriesDatumSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSeriesDatum
        fields = ['Key', 'Model', 'Instrument', 'Timestamp']

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['Name',]
