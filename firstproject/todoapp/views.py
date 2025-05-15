from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.models import User,auth 
from django.contrib.auth.hashers import make_password 
from . models import Task
from django.utils.timezone import datetime
from django.contrib import messages

# from django.contrib.auth.hashers imp


# Create your views here.


def index(request):
    return render (request,'index.html')
def navbar (request):
    return render(request,'navbar.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        Username=request.POST.get('Username')
        mobile_num=request.POST.get('mobile_num')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if password==cpassword and email not in User.objects.values_list('email',flat=True):
            hashed_password=make_password(password)
            User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=Username,password=password)
            
        return redirect('signin')

    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        Username=request.POST.get('Username')
        password=request.POST.get('password')
        User=auth.authenticate(username=Username,password=password)


        if User:
            auth.login(request,User)
            return redirect('task_details')

    return render(request,'signin.html')


def task_details(request):
    tasks = Task.objects.all()
    return render(request, "task.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        due_date = request.POST["due_date"]
        Task.objects.create(title=title, due_date=due_date)
    return redirect("task_details")

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("task_details")

def mark_finished(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = "Completed"
    task.save()
    return redirect("task_details")

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST["title"]
        task.due_date = request.POST["due_date"]
        task.save()
        return redirect("task_details")  

    return render(request, "edit_task.html", {"task": task})





