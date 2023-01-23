from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Team(models.Model):
    # id = models.IntegerField(primary_key=True,null=False)
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=200,default='team name')
    members  = models.ManyToManyField(User, related_name='teams_members')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on =models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.name

class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='channels')

    def __str__(self):
        return self.title

class Message(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.text[:20] + '...'

