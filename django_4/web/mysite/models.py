from django.db import models

# Create your models here.
class certificates(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    #image = models.ImageField()
    issued_on = models.DateTimeField(auto_now=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title