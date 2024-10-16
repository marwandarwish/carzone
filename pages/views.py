from django.shortcuts import render
from . models import Team
from cars.models import Car
from django.db.models import F ,Max

# Create your views here.


def home(request):
    teams=Team.objects.all()
    featured_car=Car.objects.order_by('create_date').filter(is_features=True)
    all_car=Car.objects.order_by('create_date').all()
    data = Car.objects.aggregate(max_price=Max('price', default=0)) 
    max_price=data['max_price']
    model=Car.objects.values_list('model',flat=True).distinct()
    state=Car.objects.values_list('state',flat=True).distinct()
    year=Car.objects.values_list('year',flat=True).distinct()
    body_style=Car.objects.values_list('body_style',flat=True).distinct()
    
    context={
       'teams':teams,
       'featured_car':featured_car,
       'all_car':all_car,
       'max_price':max_price,
       'models':model,
       'states':state,
       'years':year,
       'body_styles':body_style,
    
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


