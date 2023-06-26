from django.shortcuts import render,redirect
from .models import Register
from django.contrib import auth
from . models import Contact
from .models import Carrer
from .models import Apply


# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def choose(request):
    return render(request,'choose.html')
def classes(request):
    return render(request,'classes.html')
# def contact(request):
#     return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def team(request):
    return render(request,'team.html')
def register(request):
    return render(request,'register.html')
def reg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        obj=Register.objects.create(Name=name,Email=email,Password=password)
        obj.save()
        return redirect('/')
    return render(request,'login.html')
def login(request):
    return render(request,'login.html')


def log(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(Name=name, Password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/register')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render('/')

def contact(request):
    return render(request,'contact.html')

def contactuser(request):
    name = request.GET['n1']
    email = request.GET['e1']
    phone = request.GET['p2']
    message = request.GET['m1']
    user = Contact.objects.create(Name=name,Email=email,Phone=phone,Message=message)
    user.save()
    return render(request, 'contact.html')

def career(request):
    details = Carrer.objects.all()
    return render(request,'career.html',{'details':details})
def apply(request):
    return render(request,'apply.html')
def aply(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone = request.POST['phone']
        cv=request.POST['file_cv']
        obj=Apply.objects.create(Name=name,Email=email,Address=address,Phone=phone,CV=cv)
        obj.save()
        return redirect('/career')
    return render(request, '/')