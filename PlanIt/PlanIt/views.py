from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from PlanIt import models
from PlanIt.models import TODO

def signup(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnm,email,pwd)
        my_user=User.objects.create_user(fnm,email,pwd)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm,pwd)
    return render(request, 'login.html')
