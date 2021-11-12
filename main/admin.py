#***************************#
# django-admin startapp main
# django-admin startproject mysite
from django.contrib import admin
from main.models import Signup,Login
from django.db import models
from . import models
# from tinymce.widgets import TinyMCE
# Register your models here.
class SignupAdmin(admin.ModelAdmin):
	# fields = ["tutorial_title","tutorial_published","tutorial_content"]
	fieldsets = [("name",{"fields":["first_name", "last_name"]}),
	("Email/Password",{"fields":["email", "password"]})
	]
admin.site.register(Signup, SignupAdmin)
admin.site.register(Login)
