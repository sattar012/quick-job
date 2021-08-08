from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Contact


def signup(request):
    if request.method == 'POST':
        
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html', {'error': 'username already exits'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'] ,password=request.POST['password1'], email=request.POST['email'] ,first_name=request.POST['name'] )
                auth.login(request,user)
                return redirect('home')
    else:
        return render(request,'accounts/signup.html')

    
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html', {'error':'username or password is incorrect ' })

    else:
          return render(request,'accounts/login.html')
        

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        subject = request.POST['subject']
        message =request.POST['message']
        contact=Contact(name=name,phone=phone, email=email,subject=subject,message=message)
        contact.save()
    return render(request,'accounts/contact.html')
        

    
        
        
        
        
        
        
    
        
