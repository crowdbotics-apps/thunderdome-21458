from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PromptViewSet

router = DefaultRouter()
router.register("prompt", PromptViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
