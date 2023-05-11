from django.db import models

# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField(null=True)
    post_created = models.DateTimeField("date published")

    def __str__(self):
        return self.post_title

