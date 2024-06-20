from django.shortcuts import render
import datetime
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from conf import settings

year = datetime.date.today().year


def index(request):
    services = [
        {'name': 'Web Development', 'image': 'images/service/digital-services.png', 'description': 'Creating responsive websites.'},
        {'name': 'Mobile App Development', 'image': 'images/service/experiments.png', 'description': 'Building iOS and Android apps.'},
        {'name': 'Chatbot Development', 'image': 'images/service/chatbot.png', 'description': 'Developing whatsapp/sms chatbots.'},
        {'name': 'Python Automation', 'image': 'images/service/engineering.png', 'description': 'Automating tasks with Python.'},
        {'name': 'Generative AI Integrations', 'image': 'images/service/movies.png', 'description': 'Integrating generative AI solutions.'},
    ]
    context = {
        "year": year,
        "services": services
    }

    return render(request, 'pages/home.html',context)

def aboutUs(request):

    context = {
        "year": year,
    }

    return render(request, 'pages/about-us.html',context)

def contact(request):
    if request.method == 'POST':
        data = request.POST['values']
    context = {
        "year": year
    }
    return render(request, 'pages/contact.html',context)

@csrf_exempt
def contact(request):

    context = {
        "year": year
    }

    if request.method == 'POST':
        name =  request.POST['name']
        email =  request.POST['email']
        message =  request.POST['message']

        if not name or not email or not message:
            return JsonResponse({'info': 'error', 'message': 'All fields are required.'}, status=400)

        try:
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'info': 'success'}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'info': 'error', 'message': str(e)}, status=500)

    return render(request, 'pages/contact.html',context)

def privacyPolicy(request):

    return render(request, 'pages/privacy-policy.html')

def termOfuse(request):

    return render(request, 'pages/term-of-use.html')

    

