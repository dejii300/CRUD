from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created =models.DateTimeField(auto_now_add=True, null=True)


class Post(models.Model):
    
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models. DateTimeField(auto_now=True)
    Categories = models.ManyToManyField('Category', related_name='posts')
    image = models.ImageField(default="profile1.png", null=True, blank=True)
    def __str__(self):
        return self.title
    

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    
    

class Comment(models.Model):
    
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models. ForeignKey('post', on_delete=models.CASCADE)
            