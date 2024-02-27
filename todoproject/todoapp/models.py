from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateField(auto_now_add=True)
    deadline = models.DateField(blank=False, null=False, default=timezone.now)

    def __str__(self):
        return self.title + str("        ") + str(self.deadline)
    
    class Meta:
        ordering = ["completed"]