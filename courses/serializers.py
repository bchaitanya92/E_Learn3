from rest_framework import serializers
from .models import MITCourse

class MITCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MITCourse
        fields = '__all__'  # Include all fields in the API
