from django.db import models
from django.utils import timezone  #Add

class Post(models.Model): #means that the Post is Django Model and it should be save in DB
	author = models.ForeignKey('auth.User') #this is a link to another model
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self): # method or function
		self.published_date = timezone.now()
		self.save()

	def __str__(self):  #__ is called dunder = double underscore it returns a string
		return self.title




