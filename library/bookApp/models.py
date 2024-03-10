from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	pcs_left = models.CharField(max_length=50)
	genre =  models.CharField(max_length=150)
	cover_image = models.ImageField(upload_to='Book-Covers/', default=settings.MEDIA_URL+'no-cover.jpeg')
	rating = models.IntegerField(default=0)
	description = models.TextField(default='No description available.')		
		# borrowers

	def __str__(self):
		return self.title
	