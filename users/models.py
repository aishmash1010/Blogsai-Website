from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Profile(models.Model):
	user= models.OneToOneField(User, on_delete= models.CASCADE)
	image= models.ImageField(default='default.jpg', upload_to='profile_pics')
	bio = models.TextField()

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		#works after save, and we are overriding it 
		super().save()

		img = Image.open(self.image.path)# opens current image

		if img.height >250 or img.width> 250:
			output_size = (250,250)
			img.thumbnail(output_size)
			img.save(self.image.path)



    	
# Create your models here.
