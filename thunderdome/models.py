from django.conf import settings
from django.db import models


class Prompt(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    wordcount = models.PositiveSmallIntegerField(
        max_length=256,
        null=True,
        blank=True,
    )
    closedate = models.DateTimeField(
        null=True,
        blank=True,
    )


# Create your models here.
