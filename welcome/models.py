from django.db import models

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
	
class mytable(models.Model):
	name = models.CharField(max_length=70)
	place = models.CharField(max_length=100)

