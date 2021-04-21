from django.db import models




class TimeSeriesDatum(models.Model):
    Key = models.DateTimeField(auto_now_add=True)
    Model = models.BooleanField(default=False)
    Instrument = models.TextField(max_length=100, blank=True, default='')
    Timestamp = models.TextField()
    Value = models.TextField()

    class Meta:
        ordering = ['Timestamp']

class Instrument(models.Model):
    Name = models.TextField()
