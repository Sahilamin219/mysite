from django.db import models
from datetime import datetime
# from tinymce import HTMLField
from django.utils import timezone
# Create your models here.
class Signup(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	email = models.CharField(max_length=150)
	password = models.CharField(max_length=120)
	retype_password = models.CharField(max_length=120)
class Login(models.Model):
	email = models.CharField(max_length=150)
	password = models.CharField(max_length=120)

class Post(models.Model):
	title = models.CharField(max_length =100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	# author = models.ForeignKey(User, on_delete = models.CASCADE)

# models.DateTimeField("date published", default=datetime.now())
# content = HTMLField('Content')
# description = models.TextField(blank=True, null=True)
# content=models.TextField(null=True, blank=True)
# draft = models.BooleanField(default=False)
# def __str__(self):
# 		return self.first_name