from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Report(models.Model):
    CATEGORY_CHOICES = (
        ('ETC', 'ETC'),
        ('AEX', 'AEX'),
        ('OTR', 'OTHER'),
    )

    name = models.CharField(max_length=25)
    short_description = models.CharField(max_length=25)
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default='OTR',
    )
    description = models.TextField()
    report_url = models.URLField(max_length=200)
    file = models.FileField(
        upload_to='files',
    )
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
