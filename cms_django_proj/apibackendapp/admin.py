from django.contrib import admin
from .models import Patient,Appointment,ReceptionBill,Gender,BloodGroup, Doctor,Department,Specialization, Staff
from .models import MedicineDetails,MedicineBill,LabTestManagement,LabBill,LabReport,MedicineHistory,TestPrescription
from .models import TestPrescriptionTests,MedicinePrescription,MedicinePrescriptionMedicines
# Register your models here.
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(ReceptionBill)
admin.site.register(Gender)
admin.site.register(BloodGroup)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(Staff)
admin.site.register(MedicineDetails)
admin.site.register(MedicineBill)
admin.site.register(LabTestManagement)
admin.site.register(LabBill)
admin.site.register(LabReport)
admin.site.register(MedicineHistory)
admin.site.register(TestPrescription)
admin.site.register(TestPrescriptionTests)
admin.site.register(MedicinePrescription)
admin.site.register(MedicinePrescriptionMedicines)