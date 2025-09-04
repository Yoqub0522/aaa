from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import StudentImage


@receiver(pre_save, sender=StudentImage)
def delete_old_image_on_update(sender, instance, **kwargs):
    """StudentImage yangilansa, eski faylni o‘chirish"""
    if not instance.pk:
        return  # yangi obyekt

    try:
        old_instance = StudentImage.objects.get(pk=instance.pk)
    except StudentImage.DoesNotExist:
        return

    old_file = old_instance.image
    new_file = instance.image

    if old_file and old_file != new_file:
        if old_file.storage.exists(old_file.name):
            old_file.delete(save=False)


@receiver(post_delete, sender=StudentImage)
def delete_image_on_delete(sender, instance, **kwargs):
    """StudentImage o‘chirilganda faylni o‘chirish"""
    image = instance.image
    if image and image.storage.exists(image.name):
        image.delete(save=False)
