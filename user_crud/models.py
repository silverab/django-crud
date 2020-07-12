from django.db import models

# Create your models here.

class Position(models.Model):
	title = models.CharField(max_length=40)

	def __str__(self):
		return self.title

class Users(models.Model):
	first_name = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	mobile = models.CharField(max_length=11)
	current_status = models.ForeignKey(Position, on_delete=models.CASCADE)
	eductaion = models.CharField(max_length=30)
	city = models.CharField(max_length=20)