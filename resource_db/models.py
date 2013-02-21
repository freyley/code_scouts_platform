from django.db import models

class LearningResource(models.Model):
    url = models.URLField(max_length=2047)
    title = models.CharField(max_length=511)
    tags = models.CharField(max_length=511)
    description = models.TextField()
    cost = models.CharField(max_length=255)
    content_format = models.CharField(max_length=511, blank=True)
