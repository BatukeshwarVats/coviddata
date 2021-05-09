from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,get_object_or_404
from . models import Info
from . models import ContactForm
from django.utils import timezone
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
'''


def index(request):
    data_info=Info.objects.all()
    context={'data_info':data_info}
    return render(request,'help/index.html',context)


def ambulance(request):
    tags="AMBULANCE"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/ambulance.html',context)

def medicines(request):
    tags="MEDICINES"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/medicines.html',context)

def blood(request):
    tags="BLOOD DONOR"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/blood.html',context)

def beds(request):
    tags="BEDS"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/beds.html',context)

def consultation(request):
    tags="CONSULTATION"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/consultation.html',context)

def oxygen(request):
    tags="OXYGEN CYLINDER"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/oxygen.html',context)

def plasma(request):
    tags="PLASMA DONOR"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/plasma.html',context)

def tiffin(request):
    tags="FOOD"
    data_info=Info.objects.filter(tags=tags)
    context={'data_info':data_info}

    return render(request,'help/tiffin.html',context)

def others(request):
    tags="OTHERS"
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
    '''
def login():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('talaash')
    global sheet_instance,name,contact,tags,state,city
    sheet_instance=sheet.get_worksheet(0)
    name=sheet_instance.col_values(1)
    contact=sheet_instance.col_values(2)
    tags=sheet_instance.col_values(3)
    state=sheet_instance.col_values(4)
    city=sheet_instance.col_values(5)

login()

def index(request):
    final_data=[]
    for i in range(0,len(name)):
        final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/index.html',context)


def ambulance(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="AMBULANCE":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/ambulance.html',context)

def medicines(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="MEDICINES":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/medicines.html',context)

def blood(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="BLOOD DONOR":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/blood.html',context)

def beds(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="BEDS":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/beds.html',context)

def consultation(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="CONSULTATION":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/consultation.html',context)

def oxygen(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="OXYGEN CYLINDER":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/oxygen.html',context)

def plasma(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="PLASMA DONOR":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/plasma.html',context)

def tiffin(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="FOOD":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/tiffin.html',context)

def others(request):
    final_data=[]
    for i in range(0,len(name)):
        if tags[i]=="OTHERS":
            final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
    context={'final_data':final_data}
    return render(request,'help/others.html',context)


def search(request):
    if request.method=="POST":
        city=request.POST.get('inputCity')
        city_a=city.upper()
        state=request.POST.get('inputState')
        state_a=state.upper()
        tags=request.POST.get('tags')
        tags_a=tags.upper()
        final_data=[]
        for i in range(0,len(name)):
            if tags[i]==tags_a & state[i]==state_a & city[i]==city_a :
                final_data=final_data+[[name[i]]+[contact[i]]+[tags[i]]+[state[i]]+[city[i]]]
        context={'final_data':final_data}
        return render(request,'help/try.html',context)

def detail(request,info_id):
    data=get_object_or_404(Info,pk=info_id)
    return render(request,'help/detail.html',{'data':data})

def add(request):
    return render(request,'help/add.html')

def add_data(request):
    if request.method=="POST":
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
        data=Info(name=name,contact=contact,city=city,state=state,tags=tags)
        data.save()
    return render(request,"help/add.html")

def about(request):
    return render(request,'help/about.html')

def contactus(request):
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        contact = request.POST.get('contactus', '')
        message=request.POST.get('message','')
        contact = ContactForm(fname=fname, lname=lname, contact=contactus, message=message)
        contact.save()
    return render(request, 'help/contactus.html')