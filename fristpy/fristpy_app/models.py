from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  UserProfileInfo(models.Model):
        
        user  = models.OneToOneField(User,on_delete=models.CASCADE)
        
        profile_site = models.URLField(blank = True)

        profile_pic = models.ImageField(upload_to='imgs',blank = True)

        def __str__(self):
                return self.user.username


class testUser(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Topic(models.Model):
    topic_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.topic_name

class webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class accessrecord(models.Model):
    name = models.ForeignKey(webpage,on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return self.name