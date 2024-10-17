from django.db import models
from datetime import datetime
# Create your models here.


class Contact(models.Model):
   first_name= models.CharField( max_length=50)
   last_name= models.CharField( max_length=50)
   car_id= models.CharField( max_length=50)
   customer_need= models.CharField( max_length=50)
   car_title= models.CharField( max_length=50)
   city= models.CharField( max_length=50)
   state= models.CharField( max_length=50)
   email=models.EmailField( max_length=254)
   phone= models.CharField( max_length=50,blank=True,null=True)
   message= models.TextField(blank=True,null=True)
   user_id=models.IntegerField(blank=True,null=True)
   create_date=models.DateTimeField( default=datetime.now,blank=True,null=True)
   
   
   def __str__(self) -> str:
      return self.email