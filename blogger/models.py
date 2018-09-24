from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE
                )
    status = models.CharField(max_length=1,
                choices = (
                    ('Published', 'Published'),
                    ('Draft', 'Draft')
                ))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    blog = models.ForeignKey(
                    Blog,
                    on_delete=models.CASCADE
                )
    content = models.TextField()
    commenter = models.ForeignKey(
                     User,
                     on_delete=models.CASCADE
                 )
    created_on = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE,
                )
    user_pic = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=300)
