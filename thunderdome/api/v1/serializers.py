from rest_framework import serializers
from thunderdome.models import Prompt, Scores, Story


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"


class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = "__all__"
