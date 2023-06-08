from rest_framework import serializers
from app.models import*
class EmplayeeMS(serializers.ModelSerializer):
    class Meta:
        model=Emplayee
        fields='__all__'