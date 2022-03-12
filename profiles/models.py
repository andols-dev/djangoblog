from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profileimages',validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])]) 
    image_attribution = models.CharField(max_length=100,blank=True,null=True)
    image_attribution_name = models.CharField(max_length=100,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)  
    occupation = models.CharField(max_length=50,blank=True,null=True)
    about = models.TextField(max_length=300,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    degree = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.user.username