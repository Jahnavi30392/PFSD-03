from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def viewflights(request):
    return render(request, "viewflights.html")



def viewbookings(request):
    return render(request, "viewbookings.html")

def booking(request):
    return render(request, "booking.html")
