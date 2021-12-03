from django.db import models

from datetime import  datetime

# Create your models here.

class Blog_Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1000000)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    blog_images = models.ImageField(blank=True)
    
