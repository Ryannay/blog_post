from django.db import models
from django.utils import timezone

class Blog(models.Model):
    """Model for blog posts."""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    reading_time = models.IntegerField(default=5)  # Reading time in minutes
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    """Model for timely comments."""
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Comment {self.id}: {self.content[:30]}...'
