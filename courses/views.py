from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import MITCourse, Quest, CapstoneProject
from .serializers import (
    MITCourseSerializer,
    QuestSerializer,
    CapstoneProjectSerializer,
)


class MITCourseViewSet(viewsets.ModelViewSet):
    queryset = MITCourse.objects.all().order_by("-created_at")
    serializer_class = MITCourseSerializer


class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all().order_by("quest_number")
    serializer_class = QuestSerializer


class CapstoneProjectViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = CapstoneProject.objects.all()
    serializer_class = CapstoneProjectSerializer

    @action(detail=False, methods=["get"])
    def latest(self, request):
        capstone = self.get_queryset().order_by("-created_at").first()
        if not capstone:
            return Response({})
        return Response(self.get_serializer(capstone).data)
