from django.db import models

# Create your models here.
class certificate(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    #image = models.ImageField()
    issued_on = models.DateTimeField(auto_now=False)
    verified = models.BooleanField(default=False)