from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from . models import Info
from . models import ContactForm
from django.utils import timezone


def index(request):
    data_info=Info.objects.all()
    context={'data_info':data_info}
    return render(request,'help/index.html',context)


def ambulance(request):
    tags="Ambulance"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/ambulance.html',context)

def medicines(request):
    tags="Medicines"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/medicines.html',context)

def blood(request):
    tags="Blood Donor"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/blood.html',context)

def beds(request):
    tags="Beds"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/beds.html',context)

def consultation(request):
    tags="Consultation"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/consultation.html',context)

def oxygen(request):
    tags="Oxygen Cylinder"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/oxygen.html',context)

def plasma(request):
    tags="Plasma Donor"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/plasma.html',context)

def tiffin(request):
    tags="Food"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/tiffin.html',context)

def others(request):
    tags="Others"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/others.html',context)




def search(request):
    if request.method=="POST":
        city=request.POST.get('inputCity')
        city=city.upper()
        state=request.POST.get('inputState')
        state=state.upper()
        tags=request.POST.get('tags')
        tags=tags.upper()
        print(city)
        data_info=Info.objects.filter(city=city,state=state,tags=tags)
        print(state)
        context={'data_info':data_info}
        print(tags)
        return render(request,'help/try.html',context)

def detail(request,info_id):
    data=get_object_or_404(Info,pk=info_id)
    return render(request,'help/detail.html',{'data':data})

def add(request):
    return render(request,'help/add.html')

def add_data(request):
    if request.method=="POST":
        print(request.POST.get('name'))
        name=request.POST.get('name','')
        name=name.upper()
        contact=request.POST.get('contact','')
        contact=contact.upper()
        city=request.POST.get('city','')
        city=city.upper()
        state=request.POST.get('state','')
        state=state.upper()
        tags=request.POST.get('tags','')
        tags=tags.upper()
        print(name)
        print(contact)
        print(city)
        print(state)
        print(tags)
        data=Info(name=name,contact=contact,city=city,state=state,tags=tags)
        data.save()
        print("Data added successfully")

    return render(request,"help/add.html")

def about(request):
    return render(request,'help/about.html')

def contactus(request):
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        contact = request.POST.get('contactus', '')
        message=request.POST.get('message','')
        print(message)
        contact = ContactForm(fname=fname, lname=lname, contact=contactus, message=message)
        contact.save()
    return render(request, 'help/contactus.html')