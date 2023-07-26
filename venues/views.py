from django.shortcuts import render, redirect
from .forms import VenueForm
from .models import Venue
import pandas as pd
import requests
from io import StringIO

def venue_list(request):
    venues = Venue.objects.all()
    
    if request.method == 'POST':
        if 'delete' in request.POST:
            Venue.objects.all().delete()
            return redirect('venues:venue_list')

    return render(request, 'venue_list.html', {'venues': venues})

def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.predict_sustainability()  # Call the predict_sustainability method
            return redirect('venues:venue_list')
    else:
        form = VenueForm()

    # URL of the CSV file on GitHub
    csv_url = 'https://raw.githubusercontent.com/Yash-Bari/dataset/main/Sustain.csv'

    # Fetch the data from the URL using requests
    response = requests.get(csv_url)
    if response.status_code == 200:
        # Read the CSV data from the response content
        csv_content = response.content.decode('utf-8')
        df = pd.read_csv(StringIO(csv_content))

        events = df['Event'].unique().tolist()
        locations = df['Location'].unique().tolist()

        return render(request, 'add_venue.html', {'form': form, 'events': events, 'locations': locations})
    else:
        print(f"Failed to fetch CSV data. Status Code: {response.status_code}")
        # If fetching data fails, you can still render the form with empty events and locations
        return render(request, 'add_venue.html', {'form': form, 'events': [], 'locations': []})
