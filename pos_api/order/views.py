from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()  # Admins can see all orders
        return Order.objects.filter(user=user)  # Users see only their own orders
    
    def perform_create(self, serializer):
        """ Ensure order total_price is calculated automatically """
        order = serializer.save(user=self.request.user)

        # Recalculate total_price from order items
        total_price = sum(item.product.price * item.quantity for item in order.items.all())
        order.total_price = total_price
        order.save()  # Save updated total_price

