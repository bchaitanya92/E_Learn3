from rest_framework import viewsets
from .models import MITCourse
from .serializers import MITCourseSerializer

class MITCourseViewSet(viewsets.ModelViewSet):
    queryset = MITCourse.objects.all().order_by('-created_at')
    serializer_class = MITCourseSerializer
