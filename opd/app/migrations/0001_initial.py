# Generated by Django 4.1.5 on 2023-04-08 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Pediatrician', 'Pediatrician'), ('gynecologist', 'gynecologist'), ('Cardiologist', 'Cardiologist'), ('Oncologist', 'Oncologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Pulmonologist', 'Pulmonologist'), ('Infectious disease', 'Infectious disease'), ('Nephrologist', 'Nephrologist'), ('Endocrinologist', 'Endocrinologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Otolaryngologist', 'Otolaryngologist'), ('Dermatologist', 'Dermatologist'), ('Psychiatrist', 'Psychiatrist'), ('Neurologist', 'Neurologist'), ('Radiologist', 'Radiologist'), ('Anesthesiologist', 'Anesthesiologist'), ('Surgeon', 'Surgeon'), ('Physician executive', 'Physician executive'), ('eye', 'eye'), ('lungs', 'lungs')], max_length=100)),
                ('experiance', models.CharField(max_length=50)),
                ('appointment', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Paitent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('issue', models.CharField(choices=[('Pediatrician', 'Pediatrician'), ('gynecologist', 'gynecologist'), ('Cardiologist', 'Cardiologist'), ('Oncologist', 'Oncologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Pulmonologist', 'Pulmonologist'), ('Infectious disease', 'Infectious disease'), ('Nephrologist', 'Nephrologist'), ('Endocrinologist', 'Endocrinologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Otolaryngologist', 'Otolaryngologist'), ('Dermatologist', 'Dermatologist'), ('Psychiatrist', 'Psychiatrist'), ('Neurologist', 'Neurologist'), ('Radiologist', 'Radiologist'), ('Anesthesiologist', 'Anesthesiologist'), ('Surgeon', 'Surgeon'), ('Physician executive', 'Physician executive'), ('eye', 'eye'), ('lungs', 'lungs')], max_length=100)),
                ('appointment', models.CharField(choices=[('10:00 AM TO 11:00 AM', '10:00 AM TO 11:00 AM'), ('11:10 AM TO 12:00 PM', '11:10 AM TO 12:00 PM'), ('1:00 PM TO 2:00 PM', '1:00 PM TO 2:00 PM'), ('2:10 PM TO 3:00 PM', '2:10 PM TO 3:00 PM'), ('3:10 PM TO 4:00 PM', '3:10 PM TO 4:00 PM'), ('4:10 PM TO 5:00 PM', '4:10 PM TO 5:00 PM'), ('6:00 PM TO 7:00 PM', '6:00 PM TO 7:00 PM')], max_length=50)),
                ('approved', models.BooleanField()),
                ('report', models.CharField(max_length=50)),
                ('selectdoctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctor')),
            ],
        ),
    ]
