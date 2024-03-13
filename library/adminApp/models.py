from django.db import models
# from user_placibo import User

ST = "Student"
AD = "Admin"
SA = "Super-Admin"

ROLE_CHOICES = (
    (ST, "Student"),
    (AD, "Admin"),
    (SA, "Super-Admin"),
)

# Create your models here.
class User(models.Model):
	id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	#will change to email field with email vaidator in the future
	email  = models.EmailField(max_length=20, default='default')
	password = models.CharField(max_length=32, default='default')
	role = models.CharField(max_length=30, choices = ROLE_CHOICES, default='ST')
    # books - a backref to the Book relationship will be implemented once the book model is created

# Create your models here.
class Admin(User, models.Model):
    admin_id = models.IntegerField(primary_key=True)

class SuperAdmin(Admin, models.Model):
	super_admin_id = models.IntegerField(primary_key=True)
