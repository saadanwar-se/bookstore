from django.urls import path
from .views import CartView, AddBookToCartView, RemoveBookFromCartView, PurchaseCartView

urlpatterns = [path('detail/', CartView.as_view(), name='view-cart'),
               path('add/', AddBookToCartView.as_view(), name='add-book-to-cart'),
               path('remove/', RemoveBookFromCartView.as_view(), name='remove-book-from-cart'),
               path('purchase/', PurchaseCartView.as_view(), name='purchase-cart'),
               ]
