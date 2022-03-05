
from django.db import models

# Create your models here.
class Pure(models.Model):
    id=models.IntegerField(primary_key=True,default=True)
    name=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)

   

    
  
   