from django.shortcuts import render
from . models import Team
from cars.models import Car
from django.db.models import F
# Create your views here.


def home(request):
    teams=Team.objects.all()
    featured_car=Car.objects.order_by('create_date').filter(is_features=True)
    all_car=Car.objects.order_by('create_date').all()
   
 
    context={
       'teams':teams,
       'featured_car':featured_car,
       'all_car':all_car,
    
    }
    return render(request, 'pages/home.html',context)


def about(request):
    print(request.path)
    teams=Team.objects.all()
    context={
       'teams':teams
    }
    return render(request, 'pages/about.html',context)


def contact(request):
    return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')


