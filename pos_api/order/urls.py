from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)  # Full CRUD API for orders

urlpatterns = [
    path('', include(router.urls)),
]
