from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('add_details',views.add_details,name='add_details'),
    path('login', views.login, name='login'),
    path('contactmail',views.contactmail,name='contactmail'),


]
