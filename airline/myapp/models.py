from django.db import models

class Signup(models.Model):
    user_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    country_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name
class Booking(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    aadhar = models.CharField(max_length=12)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

    def __str__(self):
        return f"{self.fullname} - {self.origin} to {self.destination}"