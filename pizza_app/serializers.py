from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Pizza

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(Pizza.objects.all(), fields=['name', 'phone_number'])
        ]
        model = Pizza
        fields = "__all__"
