from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PromptViewSet, StoryViewSet

router = DefaultRouter()
router.register("prompt", PromptViewSet)
router.register("story", StoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
