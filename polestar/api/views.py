from django.shortcuts import render

# Create your views here.
from polestar.ships.models import Ship, Position
from rest_framework import viewsets, generics, mixins
from .serializers import ShipserSerializer, PositionsSerializer


class ShipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows ships to be viewed or edited.
    """
    queryset = Ship.objects.all().order_by('-name')
    serializer_class = ShipserSerializer


class PositionList(generics.ListAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = PositionsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        imo = self.kwargs['imo']
        return Position.objects.filter(ship__imo_number=imo).distinct()