from django.db import models
from django.contrib.auth.models import User
from book.models import Book

# Create your models here.


class Cart(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open Cart'),
        ('closed', 'Closed Cart'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"Cart for {self.user.username}"
