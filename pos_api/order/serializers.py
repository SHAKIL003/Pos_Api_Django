from rest_framework import serializers
from .models import Order, OrderItem
from product.models import Product  # Import Product for validation

class OrderItemSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField(source="product.price")  # Fetch price from Product model

    class Meta:
        model = OrderItem
        fields = ["product", "quantity", "price"]  # Include price in response

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  # Allow nested items

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'updated_at', 'items']
        read_only_fields = ['user', 'total_price', 'created_at', 'updated_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')  # Extract items

        # Remove `user` from `validated_data` because it is manually assigned later
        validated_data.pop('user', None)  

        # Create the order and assign the user manually
        order = Order.objects.create(user=self.context['request'].user, **validated_data)

        # Create order items
        for item in items_data:
            OrderItem.objects.create(order=order, **item)

        return order
