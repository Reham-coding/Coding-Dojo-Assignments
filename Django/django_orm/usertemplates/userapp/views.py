from django.shortcuts import  HttpResponse, redirect, render
from django.http import JsonResponse
from .models import User
#1 
def index(request):
    context = {}

    context["objs"]= User.objects.all()
    
   
    return render(request, "index.html", context)

def add(request):
    print("I'm ganna add ")

    firstname = request.POST['firstname']


    lastname = request.POST['lastname']

    email = request.POST['email']

    age = request.POST['age']
    


   
    
    this_user=User.objects.create(firstname =firstname, lastname = lastname, email =email, age = age) 
    request.session['id'] = this_user.id 
    # for user in User.objects.all():
        # print(user.firstname)
   
    return redirect (index)
