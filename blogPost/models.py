from django.db import models
import random
from django.contrib.auth.models import User




class Post(models.Model):
    def imageUploadPath(instance, filename):
        randomNumber = (random.randint(1,100000000))
        return ''.join(['postImg/', str(randomNumber) + filename])

    author = models.CharField(max_length=25, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=1000, null=True, blank=True)
    #install Pillow for DRF so as to use image field
    img = models.ImageField(null=True, upload_to=imageUploadPath, blank=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)
