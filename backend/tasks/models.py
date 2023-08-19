from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
