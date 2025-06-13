from django.contrib import messages
from django.shortcuts import render
from .models import register
# Create your views here.

def index(request):
    return render(request,'index.html')

def dashbord(request):
    return render(request, 'dashbord.html')

def logg(request):
    return render(request,'login.html')
def insert(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        passwd = request.POST.get("password")

        query=register(username=name, email=email, password=passwd)
        query.save()

        messages.success(request, "sign up")
        return render(request,'index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = register.objects.get(email=email, password=password)
            request.session['log_user']=user.id
            request.session.save()
        except:
            user = None
        if user is not None:
            return render(request,'dashbord.html')
        else:
            messages.info(request,"no register")
    return render(request,'login.html')