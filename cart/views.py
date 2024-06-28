from django.shortcuts import render
from .serializers import CartSerializer, CartAddBookSerializer, CartRemoveBookSerializer, CartPurchaseSerializer
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from django.shortcuts import get_object_or_404
from .models import Cart
from rest_framework.response import Response
from book.models import Book
from .utils import send_purchase_email_async
# Create your views here.


class AddBookToCartView(GenericAPIView):
    serializer_class = CartAddBookSerializer

    def post(self, request, *args, **kwargs):
        user_cart = get_object_or_404(Cart, user=request.user, status='open')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data['book_id']
            book = get_object_or_404(Book, id=book_id)
            user_cart.items.add(book)
            user_cart.save()
            return Response({'status': 'Book added'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveBookFromCartView(GenericAPIView):
    serializer_class = CartRemoveBookSerializer

    def post(self, request, *args, **kwargs):
        user_cart = get_object_or_404(Cart, user=request.user, status='open')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data['book_id']
            book = get_object_or_404(Book, id=book_id)
            user_cart.items.remove(book)
            user_cart.save()
            return Response({'status': 'Book removed'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartView(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user, status='open')


class PurchaseCartView(GenericAPIView):
    serializer_class = CartPurchaseSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        user_cart = get_object_or_404(Cart, user=user, status='open')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['confirm_purchase']:
                # Close the current cart
                user_cart.status = 'closed'
                books = user_cart.items.all()
                if books.count() > 0:
                    user_cart.save()
                    book_list = ', '.join([book.title for book in user_cart.items.all()])
                    # sending email to user
                    send_purchase_email_async(user.email, book_list)
                    # Create a new cart for the user
                    Cart.objects.create(user=user)
                    return Response({'status': 'Purchase successful, new cart created'}, status=status.HTTP_200_OK)
                else:
                    return Response({'status': 'Cart is Empty'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'status': 'Purchase not confirmed'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)