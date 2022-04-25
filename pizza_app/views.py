from django.shortcuts import render
from pizza_app.serializers import PizzaSerializer
from .models import Pizza
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet


class PizzaView(APIView):
    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response()

    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PizzaDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Pizza, pk=pk)

    def get(self, request, pk):
        serializer = PizzaSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = PizzaSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class PizzaGenericViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    