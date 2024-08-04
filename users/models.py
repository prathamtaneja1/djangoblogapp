from django.db import models
from django.contrib.auth.models import User
from PIL import Image,ExifTags
# Create your models here.

class Profile(models.Model):
    #CASCADE means that if a user is deleted then the profile is also deleted but not viceversa
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        # This method defines what is shown when an instance of the Profile model is printed
        # or viewed in the Django admin interface. It returns a string in the format:
        # "username Profile", where 'username' is the username of the associated User object.
        return f"{self.user.username} Profile"
    

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        

        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)






