from rest_framework import viewsets
from mysite.api.models import Tank
from mysite.api.serializers import TankSerializer
class TankViewSet(viewsets.ModelViewSet):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer

