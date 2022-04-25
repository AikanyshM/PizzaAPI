from datetime import datetime, date, timedelta
from urllib import request
from pizza_app.models import Pizza
from django.forms import NullBooleanField
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models.fields import NullBooleanField

class Pizza:
    def __init__(self, name, size, taste, user=User):
        self.name = name
        self.size = size
        self.taste = taste
        self.user = user 
    
pizza = Pizza(name = 'chicken', size = "large", taste="chicken_taste", user=User)
print(pizza)

user = authenticate(username='aika', password='123')
pizzas = Pizza.objects.all()

class PizzaSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)
    PIZZA_SIZE = [
        ('small', 'маленькая'),
        ('medium', 'средняя'),
        ('large', 'большая')
    ]
    size = serializers.models.CharField(
        max_length=10, 
        choices = PIZZA_SIZE, 
        default="small")
    taste = serializers.CharField(max_length=30)
    user = serializers.CurrentUserDefault(allow_null=True)

    def validate_user(self, request):
        if request.user.is_authenticated:
            return pizzas
        else:
            return None

    def add_new_order(self, request, name, size, taste, user):
        if request.user == user:
            new_pizza = Pizza.objects.create(name=name, size=size, taste=taste, user=user)
        return NullBooleanField

    def validate_size(self, size, price):
        if size == "small":
            price <= 100
        elif size == "medium":
            100 < price <= 250
        elif size == "large":
            price > 250
        return price
    
    def delete_order(self, pk, name, user):
        self.get_object(pk).delete()
        print(name, user.username)

    

serializer = PizzaSerializer(pizza, many=True, partial=True)
serializer.is_valid()
print(serializer.errors)

class Complaint:
    def __init__(self, name, phone_number, message):
        self.name = name
        self.phone_number = phone_number
        self.message = message
    
complaint = Complaint(name = request.name, phone_number=request.phone_number, message=request.message)


alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
            "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class ComplaintSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 30)
    phone_number = serializers.IntegerField()
    message = serializers.CharField(max_length = 100)

    
    def validate_name(self, name):
        if name not in alphabet and name in numbers:
            raise serializers.ValidationError('Name should not contain latin symbols and numbers')
        return name


serializer = ComplaintSerializer(complaint)
print(serializer.data)










