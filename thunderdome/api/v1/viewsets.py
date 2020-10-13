from rest_framework import authentication
from thunderdome.models import Prompt
from .serializers import PromptSerializer
from rest_framework import viewsets


class PromptViewSet(viewsets.ModelViewSet):
    serializer_class = PromptSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Prompt.objects.all()
