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
