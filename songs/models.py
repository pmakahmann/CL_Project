from django.db import models
from django.core.exceptions import ValidationError

class Song(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, default="N/A")
    composition_date = models.PositiveIntegerField(default=1900)

    
    def __str__(self):
        return self.title