from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'status']
        read_only_fields = ['user']


class CartAddBookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()


class CartRemoveBookSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()


class CartPurchaseSerializer(serializers.Serializer):
    confirm_purchase = serializers.BooleanField()