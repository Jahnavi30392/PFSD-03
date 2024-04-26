from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('viewflights/', views.viewflights, name='viewflights'),
    path('viewbookings/', views.viewbookings, name='viewbookings'),
    path('viewflights/booking/', views.booking, name='booking'),
    path("", include("myapp.urls")),  # Make sure myapp.urls is correctly defined
]
