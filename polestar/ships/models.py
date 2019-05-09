from django.db import models


class Position(models.Model):
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('date',)


class Ship(models.Model):
    name = models.CharField(max_length=70)
    imo_number = models.PositiveIntegerField(verbose_name="IMO Number")
    positions = models.ManyToManyField(Position)

    def __str__(self):
        return '{} ({})'.format(self.name, self.imo_number)

    class Meta:
        unique_together = ['name', 'imo_number']
