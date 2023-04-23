from django.contrib.auth.models import AbstractUser

from django.db import models
# User Account table
class UserAccount(AbstractUser):
    user_account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)


# Trip model
class Trips(models.Model):
    trip_id = models.AutoField(primary_key=True)
    useraccount = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)


# Destination model
class Destination(models.Model):
    destination_id = models.AutoField(primary_key=True)
    trips = models.ForeignKey(Trips, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

# Destination activity model
class Activities(models.Model):
    activity_id = models.AutoField(primary_key=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

# user registration - show profile - update profile

# dashboard - add trip - show trips - add destination - show destinations
# add activity - show activities - delete activity

