from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

UserModel = get_user_model()

class Report(models.Model):
    CATEGORY_CHOICES = (
        ('ETC', 'ETC'),
        ('AEX', 'AEX'),
        ('OTHER', 'OTHER'),
    )

    name = models.CharField(max_length=25)
    short_description = models.CharField(max_length=25)
    category = models.CharField(
        max_length=5,
        choices=CATEGORY_CHOICES,
        default='OTHER',
    )
    description = models.TextField()
    report_url = models.URLField(max_length=200)
    file = models.FileField(
        upload_to='files',
    )
    added_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)

@receiver(pre_delete, sender=Report)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(False)