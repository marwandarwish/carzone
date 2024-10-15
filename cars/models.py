from datetime import datetime 
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from multiselectfield import MultiSelectField
# Create your models here.

class Car(models.Model):
    chooise_state=(
        ('أبها','أبها'),
        ('الباحة','الباحة'),
        ('الدمام','الدمام'),
        ('الرياض','الرياض'),
        ('المدينة المنورة','المدينة المنورة'),
        ('بريدة','بريدة'),
        ('تبوك','تبوك'),
        ('جازان','جازان'),
        ('سكاكا','سكاكا'),
        ('عرار','عرار'),
        ('مكة المكرمة','مكة المكرمة'),
        ('نجران','نجران'),
        ('يشيد','يشيد'),
    )
    year_chooise=[]
    for i in range(2000,(datetime.now().year)+1):
        year_chooise.append((i,i))
    
    
    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    
    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    
    title=models.CharField(max_length=250,null=True,blank=True)
    state=models.CharField(choices=chooise_state,max_length=250,null=True,blank=True)
    city=models.CharField(max_length=250,null=True,blank=True)
    color=models.CharField(max_length=250,null=True,blank=True)
    model=models.CharField(max_length=250,null=True,blank=True)
    year=models.IntegerField(choices=year_chooise,null=True,blank=True)
    condition=models.CharField(max_length=250,null=True,blank=True)
    price=models.IntegerField(default=0)
    description=CKEditor5Field('Text', config_name='extends',max_length=5000)
    car_photo=models.ImageField(upload_to=f'photos/%Y/%m/%d/', height_field=None, width_field=None,null=True,blank=True)
    car_photo_1=models.ImageField(upload_to=f'photos/%Y/%m/%d/', height_field=None, width_field=None,null=True,blank=True)
    car_photo_2=models.ImageField(upload_to=f'photos/%Y/%m/%d/', height_field=None, width_field=None,null=True,blank=True)
    car_photo_3=models.ImageField(upload_to=f'photos/%Y/%m/%d/', height_field=None, width_field=None,null=True,blank=True)
    car_photo_4=models.ImageField(upload_to=f'photos/%Y/%m/%d/', height_field=None, width_field=None,null=True,blank=True)
    features=MultiSelectField(choices=features_choices,null=True,blank=True)
    body_style=models.CharField(max_length=250,null=True,blank=True)
    engine=models.CharField(max_length=250,null=True,blank=True)
    transmission=models.CharField(max_length=250,null=True,blank=True)
    interior=models.CharField(max_length=250,null=True,blank=True)
    miles=models.IntegerField(null=True,blank=True)
    doors=models.CharField(choices=door_choices,null=True,blank=True)
    passengers=models.IntegerField(null=True,blank=True)
    vin_no=models.CharField(max_length=250,null=True,blank=True)
    milage=models.IntegerField(null=True,blank=True)
    fuel_type=models.CharField(max_length=50,null=True,blank=True)
    no_of_owner=models.IntegerField(null=True,blank=True)
    is_features=models.BooleanField(default=False)
    create_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    discount=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.title
    
    
    def discount_offer(self):
        return self.price - (self.price * (self.discount/100))