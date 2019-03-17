from .models import NFibo
from rest_framework import serializers

class NFiboSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFibo
        fields = ('number', 'fibo')
