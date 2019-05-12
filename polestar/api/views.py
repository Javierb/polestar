from django.shortcuts import render

# Create your views here.
from polestar.ships.models import Ship, Position
from rest_framework import viewsets, generics, mixins
from .serializers import ShipserSerializer, PositionsSerializer


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows ships to be viewed.
    """
    queryset = Ship.objects.all().order_by('-name')
    serializer_class = ShipserSerializer


class PositionList(generics.ListAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows listing positions for a ship provided the imo.
    """
    serializer_class = PositionsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the positions for
        a ship in descendent order.
        """
        imo = self.kwargs['imo']
        return Position.objects.filter(ship__imo_number=imo).distinct()