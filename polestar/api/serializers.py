from rest_framework import serializers
from polestar.ships.models import Ship, Position


class ShipserSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Ship serializer that maps imo_number to imo.
    """
    imo = serializers.IntegerField(source='imo_number')
    class Meta:
        model = Ship
        fields = ('name', 'imo')


class PositionsSerializer(serializers.HyperlinkedModelSerializer):
    """
    API Position serializer that maps imo_number to imo.
    """
    class Meta:
        model = Position
        fields = ('date', 'latitude', 'longitude')