# Generated by Django 4.2.5 on 2023-09-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0006_doctor_checked_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='card_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
