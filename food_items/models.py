from django.db import models

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length=25)
    url = models.CharField(max_length=70, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    price = models.IntegerField()
    picture = models.ImageField()

    def __str__(self):
        return self.name