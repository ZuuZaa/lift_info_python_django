# from django.shortcuts import render
# from about.models import About
# from structure.models import Department, Staff
# from news.models import News
# from application.models import Application, ApplicationSubject
# from .models import FooterLink, Contact
# from operator import attrgetter

# # Create your views here.
# def home(request):

#     context = {
#         'about' : About.objects.last(),
#         'department_list' : Department.objects.all(),
#         'staff_list' : Staff.objects.all(),
#         'news_list' : sorted(News.objects.all(), key=attrgetter('published'), reverse=True)[:7],
#         'application_subjects' : ApplicationSubject.objects.all(),
#         'footer_links' : FooterLink.objects.all(),
#         'contact' : Contact.objects.last(),
#     }

#     if request.method == 'POST':

#         request_type = request.POST.get('type')
#         department = request.POST.get('structure')
#         subject = request.POST.get('theme')
#         first_name = request.POST.get('fname')
#         last_name = request.POST.get('fsurname')
#         email = request.POST.get('email')
#         prefix = str(request.POST.get('prefix'))
#         number = str(request.POST.get('fnumber'))
#         phone_number = '+994' + prefix + number
#         content = request.POST.get('fmsj')

#         new_application =Application(
#                 request_type = request_type,
#                 department = department,
#                 subject = subject,
#                 first_name = first_name,
#                 last_name = last_name,
#                 email = email,
#                 phone_number = phone_number,
#                 content = content,
#             )
#         new_application.save()

#         context['successful_submit'] = True

#     else:
#         pass

#     return render(request, 'index.html', context)


import json
import urllib

from django.shortcuts import render

from django.conf import settings
from operator import attrgetter

from about.models import About
from structure.models import Department, Staff
from news.models import News
from application.models import Application, ApplicationSubject
from .models import FooterLink, Contact


# Create your views here.
def home(request):

    context = {
        'about' : About.objects.last(),
        'department_list' : Department.objects.all(),
        'staff_list' : Staff.objects.all(),
        'news_list' : sorted(News.objects.all(), key=attrgetter('published'), reverse=True)[:7],
        'application_subjects' : ApplicationSubject.objects.all(),
        'footer_links' : FooterLink.objects.all(),
        'contact' : Contact.objects.last(),
    }

    if request.method == 'POST':

        # ''' Begin reCAPTCHA validation '''
        # recaptcha_response = request.POST.get('g-recaptcha-response')
        # url = 'https://www.google.com/recaptcha/api/siteverify'
        # values = {
        #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #     'response': recaptcha_response
        # }
        # data = urllib.parse.urlencode(values).encode()
        # req =  urllib.request.Request(url, data=data)
        # response = urllib.request.urlopen(req)
        # result = json.loads(response.read().decode())
        # ''' End reCAPTCHA validation '''

        # if result['success']:

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
             
        # else:
        #     pass

        context['successful_submit'] = True

    else:
        pass

    return render(request, 'index.html', context)
