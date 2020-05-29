from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .forms import ContactForm

def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/submission')
    context = {
    }
    return render(request, "contact.html", context)
    

    