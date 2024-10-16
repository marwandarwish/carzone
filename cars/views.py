from django.shortcuts import render , get_object_or_404
from . models import Car
from django.core.paginator import Paginator
from django.db.models import F ,Max
# Create your views here.




def cars(request):
    all_cars=Car.objects.all()
    
    car_count=all_cars.count()
    

    paginator = Paginator(all_cars, 1)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    data = Car.objects.aggregate(max_price=Max('price', default=0)) 
    max_price=data['max_price']
    model=Car.objects.values_list('model',flat=True).distinct()
    state=Car.objects.values_list('state',flat=True).distinct()
    year=Car.objects.values_list('year',flat=True).distinct()
    body_style=Car.objects.values_list('body_style',flat=True).distinct()
    

    context={
        'all_cars':page_obj,
        'car_count':car_count,
        'max_price':max_price,
        'models':model,
        'states':state,
        'years':year,
        'body_styles':body_style,
     
    }
    return render(request,'car/cars.html',context)


def car_details(request,id):
    single_car=get_object_or_404(Car,pk=id)
 
    
    context={
        'single_car':single_car,
    }
    return render(request,'car/car_details.html',context)



def search(request):
    cars=Car.objects.all()

    data = Car.objects.aggregate(max_price=Max('price', default=0)) 
    max_price=data['max_price']
    model=Car.objects.values_list('model',flat=True).distinct()
    state=Car.objects.values_list('state',flat=True).distinct()
    year=Car.objects.values_list('year',flat=True).distinct()
    transmissions_model=Car.objects.values_list('transmission',flat=True).distinct()
    body_style=Car.objects.values_list('body_style',flat=True).distinct()


    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains=keyword)
    
    
    if 'models' in request.GET:
        models=request.GET['models']
        if models:
            cars=cars.filter(model__iexact=models)
    
    if 'states' in request.GET:
        states=request.GET['states']
        if states:
            cars=cars.filter(state__iexact=states)
            
    if 'years' in request.GET:
        years=request.GET['years']
        if years:
            cars=cars.filter(year__iexact=years)
            
    if 'body_styles' in request.GET:
        body_styles=request.GET['body_styles']
        if body_styles:
            cars=cars.filter(body_style__iexact=body_styles)
    
    if 'min_price' in request.GET or 'max_price' in request.GET :
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars=cars.filter(price__gte=min_price , price__lte=max_price)
    
    if 'transmissions' in request.GET:
        transmissions=request.GET['transmissions']
        if transmissions:
            cars=cars.filter(transmission__iexact=transmissions)
    
    
    
    context={
        'cars':cars,
        'max_price':max_price,
        'models':model,
        'states':state,
        'years':year,
        'body_styles':body_style,
        'transmissions_model':transmissions_model,
    }
    return render(request,'car/search.html',context)