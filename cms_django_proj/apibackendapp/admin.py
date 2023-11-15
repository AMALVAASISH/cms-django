
# Register your models here.
from django.contrib import admin
from .models import Patient,Appointment,ReceptionBill,Gender,BloodGroup, Doctor,Department,Specialization, Staff
from .models import MedicineDetails,MedicineBill,LabTestManagement,LabBill,LabReport,MedicineHistory
from .models import MedicinePrescription,MedicinePrescriptionMedicines,Quantity

class MedicinePrescriptionAdmin(admin.ModelAdmin):
    filter_horizontal = ('medicine_id','test_id',)  # This allows multiple selections in the admin interface

# class LabTestManagementAdmin(admin.ModelAdmin):
#     filter_horizontal = ('test_id',)

admin.site.register(MedicinePrescription, MedicinePrescriptionAdmin)
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
# admin.site.register(TestPrescription)
# admin.site.register(TestPrescriptionTests)
# admin.site.register(MedicinePrescription)
admin.site.register(MedicinePrescriptionMedicines)
admin.site.register(Quantity)

