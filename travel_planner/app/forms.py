# importing the django forms.
from django import forms


# form for adding the useraccount signup / registraion details.
class UserAccountAddForm(forms.Form):
    first_name = forms.CharField(max_length=45, required=True, label="First Name")
    last_name = forms.CharField(max_length=45, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Enter Your Personal Email Address")
    phone_number = forms.CharField(max_length=10, required=True, label="Enter Your Personal Phone Number")
    password = forms.CharField(max_length=45, required=True, label="Password", help_text="Password should have "
                                                                                         "atleast  8 characters.",widget=forms.PasswordInput())


# form for adding the trip details.
class AddTripForm(forms.Form):
    name = forms.CharField(max_length=45, required=True, label="Trip Name")
    start_date = forms.DateField(required=True, label="Trip Start Date",widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    end_date = forms.DateField(required=True, label="Trip End Date",widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}))


# form for adding the destination details
class AddDestinationForm(forms.Form):
    name = forms.CharField(max_length=45, required=True, label="Destination Name")
    notes = forms.CharField(required=True, label="Add Destination Notes")


# form for adding the destination activites
class AddDestinationActivity(forms.Form):
    date = forms.DateField(required=True,label="Activity Date",widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    time = forms.TimeField(label="Destination Activity Time")
    notes = forms.CharField(required=True, label="Add Destination Activity Notes")
