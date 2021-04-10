from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User
from django.db import models
from io import BytesIO
from PIL import Image
import sys


# Create your models here.
Sex_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=6, choices=Sex_CHOICES, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics/%Y/%m/%d')
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)
    
    def __str__(self):
        return str(self.user.username)
    
    def save(self, *args, **kwargs):
		#Opening the uploaded image
        img = Image.open(self.image)
        
        im = img.convert('RGB')
        
        output = BytesIO()
        #Resize/modify the image
        im = im.resize((300,300))
        #after modifications, save it to the output

        im.save(output,"JPEG", quality=100)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super().save()