from django.shortcuts import render , redirect
from  . models import Contact
# Create your views here.

def inquery(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        user_id=request.POST['user_id']
        car_id=request.POST['car_id']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        car_title=request.POST['car_title']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        
        
        contact=Contact(first_name=first_name,last_name=last_name,customer_need=customer_need,car_title=car_title,city=city,car_id=car_id,
                        state=state,email=email,phone=phone,message=message,user_id=user_id).save()
        
        return redirect('/cars/'+car_id)