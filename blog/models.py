from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=32, null=True, unique=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    posted_at = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)

    def post(self):
        self.posted_at = timezone.now()
        self.slug = get_random_string(32)
        self.save()

    def __str__(self):
        return self.title
