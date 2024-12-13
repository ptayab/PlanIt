from django . shortcuts import render,redirect
from django.contrib.auth.models import User
from PlanIt import models
from PlanIt.models import TODO
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

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
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            auth_login(request, user)
            return redirect('/todopage')
        else:
            return redirect ('/login')
    return render(request, 'login.html')

def todopage(request):
    if request.method == 'POST':
        task=request.POST.get('task')
        print(task)
        # Show only todo by currently logged in user
        obj=models.TODO(task=task, user=request.user)
        obj.save()
    return render(request, 'todo.html')