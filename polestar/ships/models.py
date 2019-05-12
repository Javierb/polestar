from django.db import models

class CreatedUpdated(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ship(CreatedUpdated):
    name = models.CharField(max_length=70)
    imo_number = models.PositiveIntegerField(verbose_name="IMO Number")
    # positions = models.ManyToManyField(Position)

    def __str__(self):
        return '{} ({})'.format(self.name, self.imo_number)

    class Meta:
        unique_together = ['name', 'imo_number']


class Position(models.Model):
    imo_number = models.ForeignKey(Ship, on_delete=models.PROTECT, related_name="ships")
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return '{} - ({}, {})'.format(self.date, self.latitude, self.longitude)

    class Meta:
        ordering = ('-date',)
        unique_together = ["imo_number", "date"]