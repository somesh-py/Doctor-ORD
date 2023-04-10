from django.db import models

# Create your models here.
CATEGORY_ISSUE = (
    ('Pediatrician', 'Pediatrician'),
    ('gynecologist', 'gynecologist'),
    ('Cardiologist', 'Cardiologist'),
    ('Oncologist', 'Oncologist'),
    ('Gastroenterologist', 'Gastroenterologist'),
    ('Pulmonologist', 'Pulmonologist'),
    ('Infectious disease', 'Infectious disease'),
    ('Nephrologist', 'Nephrologist'),
    ('Endocrinologist', 'Endocrinologist'),
    ('Ophthalmologist', 'Ophthalmologist'),
    ('Otolaryngologist', 'Otolaryngologist'),
    ('Dermatologist', 'Dermatologist'),
    ('Psychiatrist', 'Psychiatrist'),
    ('Neurologist', 'Neurologist'),
    ('Radiologist', 'Radiologist'),
    ('Anesthesiologist', 'Anesthesiologist'),
    ('Surgeon', 'Surgeon'),
    ('Physician executive', 'Physician executive'),
    ('eye', 'eye'),
    ('lungs', 'lungs'),
)


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY_ISSUE, max_length=100)
    experiance = models.CharField(max_length=50)
    appointment = models.DateTimeField()


APPOINTMENT_TIME = (
    ('10:00 AM TO 11:00 AM', '10:00 AM TO 11:00 AM'),
    ('11:10 AM TO 12:00 PM', '11:10 AM TO 12:00 PM'),
    ('1:00 PM TO 2:00 PM', '1:00 PM TO 2:00 PM'),
    ('2:10 PM TO 3:00 PM', '2:10 PM TO 3:00 PM'),
    ('3:10 PM TO 4:00 PM', '3:10 PM TO 4:00 PM'),
    ('4:10 PM TO 5:00 PM', '4:10 PM TO 5:00 PM'),
    ('6:00 PM TO 7:00 PM', '6:00 PM TO 7:00 PM')
)


class Paitent(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=50)
    issue =models.CharField(choices=CATEGORY_ISSUE, max_length=100)
    selectdoctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)#  related_name = "name"
    appointment = models.CharField(choices=APPOINTMENT_TIME, max_length=50)
    approved = models.BooleanField()
    report = models.CharField(max_length=50)
