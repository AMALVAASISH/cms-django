from django.contrib import admin
from .models import Patient,Appointment,Bill,gender,bloodgroup, Doctor,Department,Specialization, Staff
# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Bill)
admin.site.register(gender)
admin.site.register(bloodgroup)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(Staff)