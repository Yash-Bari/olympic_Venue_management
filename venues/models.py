from django.db import models
import pandas as pd

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sustainability_facilities = models.CharField(max_length=255, null=True, blank=True)
    sustainability_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    from django.db import models
import pandas as pd
import requests
from io import StringIO

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sustainability_facilities = models.CharField(max_length=255, null=True, blank=True)
    sustainability_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    def predict_sustainability(self):
        # URL of the CSV file on GitHub
        csv_url = 'https://raw.githubusercontent.com/Yash-Bari/dataset/main/Sustain.csv'

        # Fetch the data from the URL using requests
        response = requests.get(csv_url)
        if response.status_code == 200:
            # Read the CSV data from the response content
            csv_content = response.content.decode('utf-8')
            df = pd.read_csv(StringIO(csv_content))

            # Convert the user input to lowercase
            user_name = self.name.lower()
            user_location = self.location.lower()

            # Filter the DataFrame based on the user input
            filter_df = df[
                (df['Event'].str.lower() == user_name) &
                (df['Location'].str.lower() == user_location)
            ]

            if not filter_df.empty:
                # Get the Sustainability Facilities and Score
                self.sustainability_facilities = filter_df['Sustainability Facilities'].values[0]
                self.sustainability_score = filter_df['Sustainability Venue Score'].values[0]

            self.save()
        else:
            print(f"Failed to fetch CSV data. Status Code: {response.status_code}")

