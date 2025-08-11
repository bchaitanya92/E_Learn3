from rest_framework import serializers
from .models import MITCourse, Quest, CapstoneProject


class MITCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MITCourse
        fields = "__all__"


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = [
            "id",
            "title",
            "quest_number",
            "difficulty",
            "xp",
            "icon",
            "story",
            "modules",
            "boss_battle",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class CapstoneProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapstoneProject
        fields = [
            "id",
            "title",
            "xp",
            "icon",
            "reward",
            "objective",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
