from django.db import models

class CreatedUpdated(models.Model):
    """
    Base abstract class to add auto created and updated fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ship(CreatedUpdated):
    """
    Ship model representing a ship in the DB.
    """
    name = models.CharField(max_length=70)
    imo_number = models.PositiveIntegerField(verbose_name="IMO Number")

    def __str__(self):
        return '{} ({})'.format(self.name, self.imo_number)

    class Meta:
        unique_together = ['name', 'imo_number']


class Position(models.Model):
    """
    Position model representing the position of a Ship in the DB.
    """
    ship = models.ForeignKey(Ship, on_delete=models.PROTECT, related_name="positions")
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return '{} - ({}, {})'.format(self.date, self.latitude, self.longitude)

    class Meta:
        ordering = ('-date',)
        unique_together = ["ship", "date"]