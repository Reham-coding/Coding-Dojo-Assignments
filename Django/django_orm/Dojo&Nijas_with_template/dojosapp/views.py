from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja
def index(request):
    context = {}

    context["objs"]= Dojo.objects.all()
    
   
    return render(request, "index.html", context)


    
def adddojo(request):
    print("I'm ganna add ")

    name = request.POST['name']

    state = request.POST['state']

    city = request.POST['city']
    desc = request.POST['desc']

    
    this_user=Dojo.objects.create(name =name, state = state, city =city, desc = desc) 
    request.session['id'] = this_user.id 
    # for user in User.objects.all():
        # print(user.firstname)
   
    return redirect (index)

def addNinja(request):
    print("the id ", request.POST['dojo'])

    firstname = request.POST['firstname']

    lastname = request.POST['lastname']

    id = int (request.POST['dojo'])

    this_dojo = Dojo.objects.get(id=id) 

    Ninja.objects.create(firstname =firstname, lastname = lastname, dojo =this_dojo) 
    return redirect (index)
   
