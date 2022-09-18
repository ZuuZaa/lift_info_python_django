from django.shortcuts import render
from structure.models import Department
from .models import Application, ApplicationSubject
from main.models import FooterLink, Contact

# Create your views here.
def form(request):

    context = {
        'department_list' : Department.objects.all(),
        'application_subjects' : ApplicationSubject.objects.all(),
        'footer_links' : FooterLink.objects.all(),
        'contact' : Contact.objects.last(),
    }

    if request.method == 'POST':

        request_type = request.POST.get('type')
        department = request.POST.get('structure')
        subject = request.POST.get('theme')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('fsurname')
        email = request.POST.get('email')
        prefix = str(request.POST.get('prefix'))
        number = str(request.POST.get('fnumber'))
        phone_number = '+994' + prefix + number
        content = request.POST.get('fmsj')

        new_application =Application(
                request_type = request_type,
                department = department,
                subject = subject,
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone_number = phone_number,
                content = content,
            )
        new_application.save()

        context['successful_submit'] = True

    else:
        pass

    return render(request, 'form.html', context)

