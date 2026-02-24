from django.db import models
from django.conf import settings


class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name="notes",
                              on_delete=models.CASCADE)
    title = models.TextField(default="---")
    content = models.TextField(default="---")
