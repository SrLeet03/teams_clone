from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class teams(models.Model):
    # id = models.IntegerField(primary_key=True,null=False)
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=200,default='team name')
    members  = models.ManyToManyField('User',on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on =models.DateField(default=datetime.date.today)
    
    def __init__(self, *args):
        super(teams, self).__init__(*args)
        return self.name