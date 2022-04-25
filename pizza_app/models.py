from cgitb import small
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pizza(models.Model):
    name = models.CharField(max_length=20)
    PIZZA_SIZE = [
        ('small', 'маленькая'),
        ('medium', 'средняя'),
        ('large', 'большая')
    ]
    size = models.CharField(
        max_length=10, 
        choices = PIZZA_SIZE, 
        default=small)
    taste = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

