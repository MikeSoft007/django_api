from dataclasses import field
from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class meta:
        model = Link
        field = "__all__"
        
