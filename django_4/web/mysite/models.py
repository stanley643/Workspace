from django.db import models

# Create your models here.
class certificates(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(max_length=2000)
    #image = models.ImageField()
    issued_on = models.DateTimeField(auto_now=False)
    verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['-issued_on']
        indexes = [
            models.Index(fields=['issued_on'])
        ]

    def __str__(self):
        return self.title