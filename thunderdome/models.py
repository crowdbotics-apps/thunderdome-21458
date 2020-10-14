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
        null=True,
        blank=True,
        max_length=1000,
    )


class Story(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=1000,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    prompt = models.OneToOneField(
        "thunderdome.Prompt",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="story_prompt",
    )
    wordcount = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Scores(models.Model):
    "Generated Model"
    score = models.PositiveSmallIntegerField()
    author = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="scores_author",
    )


# Create your models here.
