from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PromptViewSet, ScoresViewSet, StoryViewSet

router = DefaultRouter()
router.register("prompt", PromptViewSet)
router.register("story", StoryViewSet)
router.register("scores", ScoresViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
