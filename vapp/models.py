from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):   
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Vote(models.Model):
    item = models.ForeignKey("Item",related_name='votes',on_delete=models.CASCADE,)
    user = models.ForeignKey(User,on_delete=models.CASCADE,) 
    CHOICES = (('u', 'up'),('d', 'down'),)
    flag = models.CharField(max_length=1, choices=CHOICES)

    @property
    def int_flag(self):        
        if self.flag == 'u':return 1
        return -1 
    
