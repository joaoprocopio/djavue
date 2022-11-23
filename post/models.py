from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    posted_at = models.TimeField()
    is_deleted = models.BooleanField(default=False)

    def post(self):
        self.posted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
