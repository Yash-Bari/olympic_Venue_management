from django.shortcuts import render, redirect
from .forms import VenueForm
from .models import Venue

from django.shortcuts import render, redirect
from .models import Venue

def venue_list(request):
    venues = Venue.objects.all()
    
    if request.method == 'POST':
        if 'delete' in request.POST:
            Venue.objects.all().delete()
            return redirect('venues:venue_list')

    return render(request, 'venue_list.html', {'venues': venues})

import pandas as pd

def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.predict_sustainability()  # Call the predict_sustainability method
            return redirect('venues:venue_list')
    else:
        form = VenueForm()

    # Load the events and locations from the CSV file
    df = pd.read_csv('olympic_Venue_management/venues/Sustain.csv')  # Replace with the correct path to your CSV file
    events = df['Event'].unique().tolist()
    locations = df['Location'].unique().tolist()

    return render(request, 'add_venue.html', {'form': form, 'events': events, 'locations': locations})

