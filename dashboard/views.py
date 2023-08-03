from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render (request, 'home.html')

##############################################################################

def SignupPage(request):
    if request.method=='POST':
        username=request.POST['username'] 
        email=request.POST['email'] 
        password1=request.POST['password1'] 
        password2=request.POST['password2'] 
        
        if username=="" or email=="" or password1=="" or password2=="":
            messages.info(request,"Please fill all the fields.")
            return redirect('signup')
        
        elif password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken.")
                return redirect('signup')
          
            elif User.objects.filter(email=email).exists():
                 messages.info(request, "Email already in use.")
                 return redirect('signup')

            else:  
                user=User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password not matching")
            return redirect('signup')
  
    else:
        return render(request,'signup.html')

##########################################################################################################

def LoginPage(request):
     if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']

         user = auth.authenticate(username=username,password=password)

         if user is not None:
            auth.login(request, user)
            return redirect('home')    
         else:
           messages.info(request,'Invaild credentials.')      
           return redirect('login')

     else:
         return render(request,'login.html')
############################################################################################

def LogoutPage(request):
    logout(request)
    return redirect('login')
############################################################################################
