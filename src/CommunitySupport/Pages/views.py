from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    context = {
        "name": "Luke",
        "group": ['bread','cheese','milk'],
    }
    return render(request, "home.html", context)
    
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html")

def submission_view(request, *args, **kwargs):
    return render(request, "submission.html")