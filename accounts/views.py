from django.shortcuts import render , redirect
from django.contrib import messages ,auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as  auth_login
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout_view
from cars.models import Car
from  contact . models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('login')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('login')
        else:
            # Log in the user and redirect to the home page upon successful login
            auth_login(request, user)
            return redirect('home')
    
    # Render the login page template (GET request)
    return render(request, 'accounts/login.html')
   

    
    context={
        
    }
    return render(request,'accounts/login.html',context)

def register(request):
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request , 'User is exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request , 'email is exist')
                    return redirect('register')
                
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password,email=email)
                    auth.login(request,user=user)
                    user.save()
                    messages.success(request,'User has been added')
                    return redirect('dashboard')
        else:
            messages.error(request , 'password not match')
            return redirect('register')
    
    context={
        
    }
    return render(request,'accounts/register.html',context)


def logout(request):
    
    logout_view(request)
    return redirect('home')


# @login_required
def dashboard(request):
    user_inquery=Contact.objects.order_by('create_date').filter(user_id=request.user.id)
    context={
        'user_inquery':user_inquery,
    }
    return render(request,'accounts/dashboard.html',context)
