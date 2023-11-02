from django.db import models

# Create your models here.

class todos(models.Model):
    task = models.CharField(max_length=250)
    time = models.DateTimeField(default=False)
    completed = models.BooleanField(default=False)
    comments = models.TextField(max_length=250)