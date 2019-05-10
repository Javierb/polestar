from rest_framework import serializers
from polestar.ships.models import Ship, Position


class ShipserSerializer(serializers.HyperlinkedModelSerializer):
    imo = serializers.IntegerField(source='imo_number')
    class Meta:
        model = Ship
        fields = ('name', 'imo')


class PositionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('date', 'latitude', 'longitude')