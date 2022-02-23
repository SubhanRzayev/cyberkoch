from rest_framework import serializers
from core.models import Subscriber

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
        )