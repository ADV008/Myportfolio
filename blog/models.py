from django.db import models



class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField(null='True')
	body = models.TextField(null='True')
	image = models.ImageField(upload_to='images/')