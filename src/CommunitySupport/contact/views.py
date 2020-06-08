from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .forms import ContactForm
from .email import contact_send_email

def contact_create_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.email,form.name)
        return redirect('/submission')
    context = {
    }
    return render(request, "contact.html", context)
    

    