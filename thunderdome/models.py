from django.conf import settings
from django.db import models


class Prompt(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=256,
    )


# Create your models here.
