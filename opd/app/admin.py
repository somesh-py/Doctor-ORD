from django.contrib import admin
from .models import *
# Register your models here.


@admin.register((Doctor))
class DoctorModelAdmin(admin.ModelAdmin):
    list_display=['id','category','experiance','appointment']

@admin.register((Paitent))
class PatientModelAdmin(admin.ModelAdmin):
    list_display=['id','name','contact','email','address','issue','selectdoctor','appointment','approved','report']