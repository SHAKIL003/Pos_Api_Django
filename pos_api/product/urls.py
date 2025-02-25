from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # This automatically creates CRUD routes
router.register(r'categories', CategoryViewSet)  # Add category routes

urlpatterns = [
    path('', include(router.urls)),
]
