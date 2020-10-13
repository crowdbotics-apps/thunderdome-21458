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
        null=True,
        blank=True,
        max_length=256,
    )
    closedate = models.DateTimeField(
        null=True,
        blank=True,
    )


class Story(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=1000,
    )


# Create your models here.
