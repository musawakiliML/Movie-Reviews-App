from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=200)
    tagline = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/news/')
    date = models.DateField()
    
    
    def __str__(self):
        return self.headline
    