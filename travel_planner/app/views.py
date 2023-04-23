from django.shortcuts import render

from .forms import UserAccountAddForm, AddTripForm, AddDestinationForm, AddDestinationActivity

from .models import UserAccount, Trips, Destination, Activities

from django.shortcuts import redirect

from allauth.account.utils import perform_login

from allauth.account import app_settings as allauth_settings
# this python function will using for adding and updating the customer details
def add_or_update_customer_account(request, user_account_id=None):
    if request.method == "POST":
        post_form = UserAccountAddForm(request.POST)
        if user_account_id:
            useraccount = UserAccount.objects.filter(user_account_id=user_account_id).first()
        else:
            useraccount = ''
        if post_form.is_valid():
            first_name = post_form.cleaned_data["first_name"]
            last_name = post_form.cleaned_data["last_name"]
            phone_number = post_form.cleaned_data["phone_number"]
            email = post_form.cleaned_data["email"]
            password = post_form.cleaned_data["password"]
            if user_account_id:
                useraccount.first_name = first_name
                useraccount.last_name = last_name
                useraccount.phone_number = phone_number
                useraccount.email = email
                useraccount.save()
                perform_login(request, useraccount, allauth_settings.EMAIL_VERIFICATION, signup=False,
                              redirect_url=None, signal_kwargs=None)
                return redirect('user_profile')
            else:
                useraccount = UserAccount.objects.create(first_name=first_name, last_name=last_name,
                                                         phone_number=phone_number,
                                                         username=phone_number,
                                                         email=email)
                useraccount.set_password(password)
                useraccount.save()
                perform_login(request, useraccount, allauth_settings.EMAIL_VERIFICATION, signup=False,
                              redirect_url=None, signal_kwargs=None)
                return redirect('home_page')
    else:
        post_form = UserAccountAddForm()
        if not request.user.is_active:
            return render(request, 'customer_registration.html',
                          {'form': post_form, 'user_account_id': user_account_id})
        post_form.fields["first_name"].initial = request.user.first_name
        post_form.fields["last_name"].initial = request.user.last_name
        post_form.fields["email"].initial = request.user.email
        post_form.fields["phone_number"].initial = request.user.phone_number
        return render(request, 'customer_registration.html', {'form': post_form, 'user_account_id': user_account_id})

from datetime import datetime
def home_page(request):
    if not request.user.is_active:
        return redirect('user_registration')
    return render(request, 'plan_trip_dashboard.html')

def show_user_profile(request):
    return render(request,'show_customer_profile.html')

def add_or_update_customer_trip_details(request, trip_id=None):
    if trip_id:
        trip = Trips.objects.filter(trip_id=trip_id).first()
    else:
        trip = ''
    if request.method == "POST":
        trip_form = AddTripForm(request.POST)

        if trip_form.is_valid():
            name = trip_form.cleaned_data["name"]
            start_date = trip_form.cleaned_data["start_date"]
            end_date = trip_form.cleaned_data["end_date"]
            if trip_id:
                trip.name = name
                trip.end_date = end_date
                trip.start_date = start_date
                trip.save()
                return redirect('show_trips')
            else:
                trip = Trips.objects.create(name=name, start_date=start_date,
                                            end_date=end_date,useraccount=request.user)
                return redirect('show_trips')
        print(trip_form.errors)
    else:
        trip_form = AddTripForm()
        if trip_id:
            trip_form.fields["name"].initial = trip.name

            state_date = datetime.strptime(str(trip.start_date), '%Y-%m-%d').strftime('%m/%d/%Y')
            end_date = datetime.strptime(str(trip.end_date), '%Y-%m-%d').strftime('%m/%d/%Y')
            trip_form.fields["start_date"].initial = state_date
            trip_form.fields["end_date"].initial = end_date
        return render(request, 'add_trip.html', {'form': trip_form, 'trip_id': trip_id})


def show_trips(request):
    trips = Trips.objects.filter(useraccount=request.user)
    return render(request, 'show_trips.html', {'trips': trips})


def add_or_update_customer_destination_details(request, trip_id, destination_id=None):
    trip = Trips.objects.filter(trip_id=trip_id).first()

    if request.method == "POST":
        destination_form = AddDestinationForm(request.POST)
        if destination_form.is_valid():
            name = destination_form.cleaned_data["name"]
            notes = destination_form.cleaned_data["notes"]
            if destination_id:
                destination = Destination.objects.filter(destination_id=destination_id).first()
                destination.name = name
                destination.notes = notes
                destination.save()
                return redirect('show_trips')
            else:
                destination = Destination.objects.create(name=name, notes=notes,trips=trip)
                return redirect('show_trips')
        print(destination_form.errors)
    else:
        destination_form = AddDestinationForm()
        if destination_id:
            destination = Destination.objects.filter(destination_id=destination_id).first()
            destination_form.fields["name"].initial = destination.name
            destination_form.fields["notes"].initial = destination.notes
        return render(request, 'add_trip_destination.html', {'form': destination_form, 'trip_id': trip_id,'destination_id':destination_id})


def show_destinations(request, trip_id):
    trip = Trips.objects.filter(trip_id=trip_id).first()
    destinations = Destination.objects.filter(trips__pk=trip_id)
    return render(request, 'show_destinations.html', {'destinations': destinations,'trip':trip})


def delete_trip_details(request,trip_id):
    Trips.objects.filter(trip_id=trip_id).delete()
    return redirect('show_trips')

def delete_destinations(request, destination_id):
    Destination.objects.filter(destination_id=destination_id).delete()
    return redirect('show_trips')


def add_or_update_trip_destination_activites_details(request, destination_id, activity_id=None):
    destination = Destination.objects.filter(destination_id=destination_id).first()
    if request.method == "POST":
        activity_form = AddDestinationActivity(request.POST)
        if activity_form.is_valid():
            time = activity_form.cleaned_data["time"]
            date = activity_form.cleaned_data["date"]
            notes = activity_form.cleaned_data["notes"]
            if activity_id:
                activity = Activities.objects.filter(activity_id=activity_id).first()
                activity.notes = notes
                activity.destination = destination
                activity.time = time
                activity.save()
                return redirect('show_trips')
            else:
                activity = Activities.objects.create(date=date, notes=notes, time=time, destination=destination)
                return redirect('show_trips')
        print(activity_form.errors)
    else:
        activity_form = AddDestinationActivity()
        if activity_id:
            activity = Activities.objects.filter(activity_id=activity_id).first()
            activity_date = datetime.strptime(str(activity.date), '%Y-%m-%d').strftime('%m/%d/%Y')
            activity_form.fields["notes"].initial = activity.notes
            activity_form.fields["time"].initial = activity.time
            activity_form.fields["date"].initial = activity_date
        return render(request, 'add_destination_activity.html', {'form': activity_form, 'destination_id': destination_id
            , 'activity_id': activity_id})


def show_activites(request, destination_id):
    activites = Activities.objects.filter(destination__pk=destination_id)
    return render(request, 'show_destination_activites.html', {'activites': activites})


def delete_activity(request, activity_id):
    Activities.objects.filter(activity_id=activity_id).delete()
    return redirect('show_trips')
