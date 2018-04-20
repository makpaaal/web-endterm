from django.db import models
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save

	def to_json(self):
  		return{
  		'id': self.id,
  		'title': self.title,
  		'text': self.text,
  		'published_date': self.published_date,
  		}

	def __str__(self):
		return self.title
