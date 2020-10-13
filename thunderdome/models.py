from django.conf import settings
from django.db import models


class Prompt(models.Model):
    "Generated Model"
    content = models.TextField(
        null=True,
        blank=True,
    )
    closedate = models.DateTimeField(
        null=True,
        blank=True,
    )
    wordcount = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
    )


class Story(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=1000,
    )


# Create your models here.
