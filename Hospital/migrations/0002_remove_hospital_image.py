# Generated by Django 4.2.5 on 2023-09-23 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='image',
        ),
    ]
