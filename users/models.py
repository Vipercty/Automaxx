from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path

class Location(models.Model):
    address_1 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to= user_directory_path,null = True)
    bio = models.CharField(max_length=50, blank= True)
    phone_number = models.CharField( max_length=10, blank = True)
    location = models.OneToOneField(Location,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    


