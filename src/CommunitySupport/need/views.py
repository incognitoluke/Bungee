from django.shortcuts import render
from django.shortcuts import redirect
from .models import Order, Donation
from .form import OrderForm, DonationForm
import datetime
from .sort import sort_orders

import itertools
#import itertools

# Create your views here.




def order_view(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        town = request.POST.get('Town')
        address = request.POST.get('Address')
        email = request.POST.get('Email')
        number = request.POST.get('Number')
        urgency = request.POST.get('Urgency')
        Non_Perishable = request.POST.get('Non-perishable')
        Perishable = request.POST.get('Perishable')
        terms = request.POST.get('terms')
        time = datetime.datetime.now()
        print(name,town,address,email,number,Non_Perishable,Perishable,terms,time)
        Order.objects.create(name=name,address=address,town=town,email=email,number=number,urgency=urgency,Non_Perishable=Non_Perishable,Perishable=Perishable,terms=terms,time=time)
        #alert_email(name)
        return redirect('/submission')
    context = {}
    return render(request, "order.html", context)

def order_list_view(request):
    queryset = Order.objects.all()
    

    approved = []
    for item in queryset:
        if item.featured == True:
            approved.append(item)
        else: 
            continue
    
    sort_orders(approved)

    queryset = Order.objects.all().order_by('score')
    queryset = queryset.reverse()

    approved = []
    for item in queryset:
        if item.featured == True:
            approved.append(item)
        else: 
            continue

    
    Non_Perishable = []
    Perishable = []
    for item in approved:
        Non_Perishable.append((item.Non_Perishable).split(","))
        Perishable.append((item.Perishable).split(","))

    for (obj,item,item_two) in zip(approved,Non_Perishable,Perishable):

        obj.Non_Perishable = item
        obj.Perishable = item_two

    list_length = len(approved)
    context = {
        "object_list": approved,
        "non-perishable": Non_Perishable,
        "length": list_length
    }
    return render(request, "donation_list.html", context)

def dynamic_order_view(request, id):
    obj = Order.objects.get(id=id)


    np = (obj.Non_Perishable).split(",")
    p = (obj.Perishable).split(",")

    for (w,z) in zip(np,p):
        w = w.capitalize()
        z = z.capitalize()

    obj.Non_Perishable = np
    obj.Perishable = p
    
    if request.method == "POST":
        name = request.POST.get('Name')
        town = request.POST.get('Town')
        address = request.POST.get('Address')
        email = request.POST.get('Email')
        number = request.POST.get('Number')
        donation = request.POST.getlist('Donation')
        terms = request.POST.get('Terms')
        time = datetime.datetime.now()
        print(name,town,address,email,number,donation,terms,time)
        Donation.objects.create(name=name,address=address,town=town,email=email,number=number,donation=donation,terms=terms,time=time)
        #alert_email(name)
        return redirect('/submission')

    context = {
        "object": obj
    }
    return render(request, "donation/donation.html", context)


