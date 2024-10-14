from django.db import models

# Create your models here.


class Team(models.Model):
    first_name=models.CharField(max_length=250,blank=True,null=True)
    last_name=models.CharField(max_length=250,blank=True,null=True)
    designation=models.CharField(max_length=250,blank=True,null=True)
    phtoto=models.ImageField(upload_to='photos/%Y/%m/%d/', height_field=None, width_field=None, max_length=None)
    facebook=models.URLField(max_length=200)
    twitter=models.URLField(max_length=200)
    google=models.URLField(max_length=200)
    create_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    
    
    
    def __str__(self) -> str:
        return self.first_name+' '+self.last_name
