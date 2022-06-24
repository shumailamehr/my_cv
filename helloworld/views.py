import encodings
from django.shortcuts import render, HttpResponse

from.models import User_details
#to import os mudule
import os
# Create your views here.

def show_login(request):
    # return HttpResponse('SHUMAILA   ANDLEEB')
    # ,encodings="utf-8"
    return render (request, "loginpage.html")

def show(request):
    # return HttpResponse('SHUMAILA   ANDLEEB')
    # ,encodings="utf-8"
    return render (request, "index.html")

    #to get data from user
def get_data(request):
    name = request.POST['name']
    print(name)
    mail = request.POST['dingdong']
    print(mail)
    msg = request.POST['message']
    print(msg)
    a = User_details(Name=name,Email=mail,message=msg)
# declare variable to save data in sqlite
    a.save()
    return HttpResponse('Data sent to databade successfully')

