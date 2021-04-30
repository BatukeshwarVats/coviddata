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

def search(request):
    if request.method=="POST":
        city=request.POST.get('inputCity')
        state=request.POST.get('inputState')
        tags=request.POST.get('tags')
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
        print(request)
        print(request.POST.get('name'))
        name=request.POST.get('name','')
        contact=request.POST.get('contact','')
        address=request.POST.get('address','')
        disc=request.POST.get('disc','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        tags=request.POST.get('tags','')
        print(name)
        print("Hey sexy")
        data=Info(name=name,contact=contact,address=address,disc=disc,city=city,state=state,tags=tags)
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