from django.db import models

# Create your models here.
class Book(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	genre =  models.CharField(max_length=150)
	