from django.db import models


class MITCourse(models.Model):
    title = models.CharField(max_length=300)
    subject = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Quest(models.Model):
    title = models.CharField(max_length=255)
    quest_number = models.PositiveIntegerField(unique=True)
    difficulty = models.PositiveSmallIntegerField()  # 1-5
    xp = models.PositiveIntegerField()
    icon = models.CharField(max_length=16)  # emoji or short SVG/text
    story = models.TextField()
    modules = models.JSONField(default=list)
    boss_battle = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["quest_number"]

    def __str__(self) -> str:
        return f"Quest {self.quest_number}: {self.title}"


class CapstoneProject(models.Model):
    title = models.CharField(max_length=255)
    xp = models.PositiveIntegerField()
    icon = models.CharField(max_length=16)
    reward = models.CharField(max_length=255)
    objective = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
