from rest_framework import serializers
from mysite.api.models import Tank
class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ('model_name', 'caliber', 'weight')
