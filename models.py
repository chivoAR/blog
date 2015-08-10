from django.db import models
from django     import template
from itertools import permutations

register=template.Library()

# Create your models here.
class Post(models.Model):
     title =  models.CharField(max_length = 100)
     body = models.TextField()
     date = models.DateTimeField() 
     def _unicode_(self): 
     
          return self.title
     def all_perms(s):
     #function return itertools.permutations('abc')
       print (' haloooooooooooooooooooo')
               
@register.filter
def myfilter(obj, epk):
      print (' haloooooooooooooooooooo')
