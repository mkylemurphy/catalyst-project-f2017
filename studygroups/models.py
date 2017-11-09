from django.db import models


class Event(models.Model):
    # TODO: check that these 3 fields are
    # mutually exclusive for each Event
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name




