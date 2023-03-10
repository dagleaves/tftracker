from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Collection


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_collections(sender, instance, created, **kwargs):
    if created:
        collection = Collection.objects.create(user=instance, name='Collection', public=True)
        wishlist = Collection.objects.create(user=instance, name='Wishlist', public=True)
        collection.save()
        wishlist.save()