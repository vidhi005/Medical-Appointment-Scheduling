# Generated by Django 4.2.5 on 2023-09-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0004_appointment_patient_name_alter_appointment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient_name',
        ),
    ]
