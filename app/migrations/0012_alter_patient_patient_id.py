# Generated by Django 3.2.3 on 2021-06-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_patient_patient_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
