from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from pizza_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pizza', views.PizzaGenericViewSet, basename='pizza')

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.PizzaView.as_view()),
    #path('pizza/<int:pk>/', views.PizzaDetailView.as_view()),
    path('', include(router.urls)),
    
]
