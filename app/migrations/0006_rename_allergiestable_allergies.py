# Generated by Django 3.2.3 on 2021-06-08 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210608_2047'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllergiesTable',
            new_name='Allergies',
        ),
    ]