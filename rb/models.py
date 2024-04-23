from django.db import models

# Create your models here.
class Rider(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.username