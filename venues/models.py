from django.db import models
import pandas as pd

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    sustainability_facilities = models.CharField(max_length=255, null=True, blank=True)
    sustainability_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    def predict_sustainability(self):
        # Load the data from the CSV file
        df = pd.read_csv(r'C:\Users\Yash\sustainability_venue_app\venues\Sustain.csv')  # Replace with the correct path to your CSV file

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
