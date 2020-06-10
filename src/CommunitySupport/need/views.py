from django.shortcuts import render
from django.shortcuts import redirect
from .models import Order, Donation
from .form import OrderForm, DonationForm
import datetime
from .sort import sort_orders
from .email import alert_email

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

"""def region_donation(request):

    towns_list = ['Allendale','Alpine', 'Bergenfield', 'Bogota', 'Carlstadt', 'Cliffside Park', 'Closter', 'Cresskill', 'Demarest', 'Dumont', 'East Rutherford', 'Edgewater', 'Elmwood Park', 'Emerson', 'Englewood', 'Englewood Cliffs', 'Fair Lawn', 'Fairview', 'Fort Lee', 'Franklin Lakes', 'Garfield', 'Glen Rock', 'Hackensack', 'Harrington Park', 'Hasbrouck Heights', 'Haworth', 'Hillsdale', 'Ho Ho Kus', 'Leonia', 'Little Ferry', 'Lodi', 'Lyndhurst', 'Mahwah', 'Maywood', 'Midland Park', 'Montvale', 'Moonachie', 'New Milford', 'North Arlington', 'Northvale', 'Norwood', 'Oakland', 'Old Tappan', 'Oradell', 'Palisades Park', 'Paramus', 'Park Ridge', 'Ramsey', 'Ridgefield', 'Ridgefield Park', 'Ridgewood', 'River Edge', 'River Vale', 'Rochelle Park', 'Rockleigh', 'Rutherford', 'Saddle Brook', 'Saddle River', 'South Hackensack', 'Teaneck', 'Tenafly', 'Teterboro', 'Upper Saddle River', 'Waldwick', 'Wallington', 'Washington Township', 'Westwood', 'Woodcliff Lake', 'Wood-Ridge', 'Wyckoff']

    if request.method == "POST":
        Town = request.POST.get('Town')
        return redirect('/donate/' + Town)
    
    context = {
        "towns_list": towns_list,
    }

    return render(request, "donation_region.html", context)"""

#add town to sort
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
        obj.town = (obj.town).title()

    list_length = len(approved)
    context = {
        "object_list": approved,
        "non-perishable": Non_Perishable,
        "length": list_length,
        #"town": town,
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
        
        alert_email(name, email, donation)
        return redirect('/submission')

    context = {
        "object": obj
    }
    return render(request, "donation/donation.html", context)


