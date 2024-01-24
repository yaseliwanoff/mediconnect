# Generated by Django 5.0.1 on 2024-01-24 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_time', models.CharField(verbose_name='Available time')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
                ('first_name', models.CharField(max_length=80, verbose_name='First name')),
                ('last_name', models.CharField(max_length=80, verbose_name='Last name')),
                ('about', models.TextField(blank=True, max_length=600, verbose_name='Information about doctor')),
                ('experience', models.TextField(blank=True, verbose_name='Experience')),
                ('price', models.IntegerField(blank=True, default=None, verbose_name='Visit price')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80, verbose_name='First name')),
                ('last_name', models.CharField(max_length=80, verbose_name='Last name')),
                ('phone_number', models.CharField(max_length=18, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='SpecializationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization_title', models.CharField(verbose_name='Specialization title')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_datetime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.appointmenttime')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.patient')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='main.specializationcategory'),
        ),
    ]
