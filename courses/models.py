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
