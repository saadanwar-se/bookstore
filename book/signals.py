from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cart.models import Cart


@receiver(post_save, sender=User)
def make_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)