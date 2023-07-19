# Generated by Django 3.2.18 on 2023-07-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('sustainability_facilities', models.CharField(blank=True, max_length=255, null=True)),
                ('sustainability_score', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
