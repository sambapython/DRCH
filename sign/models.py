from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser

class Submenu(models.Model):
	name = models.CharField(max_length=250)
	url = models.CharField(max_length=250)
	def __str__(self):
		return "%s-->%s"%(self.name, self.url)
class Menu(models.Model):
	name = models.CharField(max_length=250)
	submenus = models.ManyToManyField(Submenu, blank=True, null=True)
	def __str__(self):
		return "%s"%(self.name)


class Role(models.Model):
	name = models.CharField(max_length=10, 
		choices=[("user","User"),("admin","admin")],
		default="user")
	menus= models.ManyToManyField(Menu, blank=True)

	def __str__(self):
		return self.name
class UserProfile(AbstractUser):
	role = models.ForeignKey(Role, on_delete=models.PROTECT, blank=True,
		null=True)

class Claim(models.Model):
	amount = models.IntegerField(default=0)
	description = models.TextField(default="")
	user = models.ForeignKey(UserProfile,blank=True, null=True, on_delete=models.PROTECT)

class Visit(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
	datetime = models.DateTimeField(default=timezone.now)
	payment = models.IntegerField(default=0)
	cause = models.TextField(default="")
	status = models.BooleanField(default=True)