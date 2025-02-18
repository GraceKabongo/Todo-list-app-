from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from  uuid import uuid4

# Create your models here.
class TaskModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4())
    title = models.CharField(max_length=280)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title