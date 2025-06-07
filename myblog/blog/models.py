from django.db import models

# Create your models here.
from django.utils import timezone
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField()
    Created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

