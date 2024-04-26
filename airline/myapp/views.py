from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup
from django.core.mail import send_mail
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Signup.objects.get(user_name=username, password=password)
            # If user exists, redirect to some other page, e.g., dashboard
            # Replace 'dashboard' with your desired URL
            return render(request, 'home.html')
        except Signup.DoesNotExist:
            # If user doesn't exist, render login page again with an error message
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def add_details(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email_id = request.POST.get('email_id')
        password = request.POST.get('password')
        age = request.POST.get('age')
        country_name = request.POST.get('country_name')
        mobile_number = request.POST.get('mobile_number')

        if Signup.objects.filter(user_name=user_name).exists() or Signup.objects.filter(email_id=email_id).exists():
            return render(request, 'signup.html', {'error': 'An account with this username or email already exists.'})
        else:
            # Save user details
            user_details = Signup(
                user_name=user_name,
                email_id=email_id,
                password=password,
                age=age,
                country_name=country_name,
                mobile_number=mobile_number,
            )
            user_details.save()
            return redirect('login')
    return render(request, 'index.html')

def contactmail(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject,message,'samudralajahnavi0806@gmail.com',['samudralajahnavi0806@gmail.com'],fail_silently=False)
        return HttpResponse("Mailsent Successfully")

    else:
        return render(request,'mail.html')


def home(request):
    return render(request, 'home.html')


