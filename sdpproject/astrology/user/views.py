from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import registerForm
from .models import register


def home(request):
    return render(request, "base.html")


def registration(request):
    form1 = registerForm()
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request, "register.html", {"msg": msg, "form": form1})
        else:
            msg = "Failed Registration"
            return render(request, "register.html", {"msg": msg, "form": form1})
    return render(request, "register.html", {"form": form1})


def checklogin(request):
    uname = request.POST["uname"]
    pwd = request.POST["pwd"]

    flag = register.objects.filter(Q(username=uname) & Q(password=pwd))
    # print(flag)
    if flag:
        # print("login sucess")
        return render(request, "userhome.html")
    else:
        msg = "Incorrect username or password"
        return render(request, "userlogin.html", {"message": msg})


def updatepwd(request):
    opwd = request.POST['opwd']
    npwd = request.POST['npwd']
    print(opwd, npwd)
    flag = register.objects.filter(Q(password=opwd))
    if flag:
        register.objects.filter(password=opwd).update(password=npwd)
        msg = "Password Updated Sucessfully"
    else:
        msg = "Old password is incorrect"
    return render(request, 'changepassword.html', {"message": msg})


def login(request):
    return render(request, "userlogin.html")


def about(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')


def zodiacsign(request):

    return render(request, 'zodiacsign.html')


def horoscope(request):
    return render(request, 'horoscope.html')

def changepassword(request):
    return render(request,'changepassword.html')