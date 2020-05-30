from django.shortcuts import render
from django.shortcuts import redirect
from .models import Volunteer
from .forms import VolunteerForm
import datetime

# Create your views here.




def volunteer_view(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        town = request.POST.get('Town')
        email = request.POST.get('Email')
        number = request.POST.get('Number')
        age = request.POST.get('defaultExampleRadios')
        terms = request.POST.get('Terms')
        time = datetime.datetime.now()
        print(name,town,email,number,age,terms,time)
        Volunteer.objects.create(name=name,town=town,email=email,number=number,age=age,terms=terms,time=time)
        return redirect('/submission')
    context = {}
    return render(request, "volunteer.html", context)