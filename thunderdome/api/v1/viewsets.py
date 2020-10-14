from rest_framework import authentication
from thunderdome.models import Prompt, Scores, Story
from .serializers import PromptSerializer, ScoresSerializer, StorySerializer
from rest_framework import viewsets


class PromptViewSet(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Prompt.objects.all()


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Story.objects.all()


class ScoresViewSet(viewsets.ModelViewSet):
    serializer_class = ScoresSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Scores.objects.all()
