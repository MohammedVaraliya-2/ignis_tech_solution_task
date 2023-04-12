from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/')
    is_liked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.event_name