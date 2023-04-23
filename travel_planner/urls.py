"""travel_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/',add_or_update_customer_account,name='user_registration'),
    path('',home_page,name='home_page'),
    path('show/user/profile/',show_user_profile,name='user_profile'),
    path('update/user/profile/<int:user_account_id>/',add_or_update_customer_account,name='update_profile'),

    path('add/trip/',add_or_update_customer_trip_details,name='add_trip'),
    path('show/trips/',show_trips,name='show_trips'),
    path('update/trip/details/<int:trip_id>/',add_or_update_customer_trip_details,name='update_trip_profile'),
    path('delete/trip/details/<int:trip_id>/',delete_trip_details,name='delete_trip_profile'),

    path('add/destination/<int:trip_id>/',add_or_update_customer_destination_details,name='add_destination'),
    path('show/destinations/<int:trip_id>/',show_destinations,name='show_destinations'),
    path('update/destination/details/<int:trip_id>/<int:destination_id>/',add_or_update_customer_destination_details,name='update_destination_details'),
    path('delete/destination/details/<int:destination_id>/',delete_destinations,name='delete_trip_profile'),

    path('add/activity/<int:destination_id>/',add_or_update_trip_destination_activites_details,name='add_activity'),
    path('show/activities/<int:destination_id>/',show_activites,name='show_activities'),
    path('update/activity/details/<int:destination_id>/<int:activity_id>/',add_or_update_customer_destination_details,name='update_activity_details'),
    path('delete/activity/details/<int:activity_id>/',delete_activity,name='delete_activity'),



]
