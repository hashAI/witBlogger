from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import hashlib

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

def profile_pic_path(instance, filename):
    filename = hashlib.md5(str(instance.user.id).encode()+str(filename).encode()+(str(timezone.now()).encode())).hexdigest()
    return "profile_pics/user_{0}/{1}".format(instance.user.id, filename)

class UserProfile(models.Model):
    user = models.OneToOneField(
                    User,
                    on_delete=models.CASCADE,
                    primary_key=True,
                )
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    user_pic = models.FileField(max_length=500, upload_to=profile_pic_path, blank=True, null=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    hobbies = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)

