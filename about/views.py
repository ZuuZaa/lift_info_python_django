from django.shortcuts import render
from .models import About
from main.models import FooterLink, Contact

# Create your views here.
def about(request):

    context = {
        'about' : About.objects.last(),
        'footer_links' : FooterLink.objects.all(),
        'contact' : Contact.objects.last(),
    }
    return render(request, 'about.html', context)

