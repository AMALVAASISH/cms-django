from rest_framework import serializers
from .models import Doctor,Department,Staff,Specialization,User,Appointment,Patient,ReceptionBill,Gender,BloodGroup, MedicineDetails, MedicineBill
from .models import MedicinePrescription, Quantity
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class SpecialisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
# ===============================================================
# ================================================================
class DoctorSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='staff.name')
    specialisation = serializers.CharField(source='specialization')
    class Meta:
        model = Doctor
        fields = '__all__'

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class BloodgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodGroup
        fields = '__all__'
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor_id.staff.name')
    specialisation = serializers.CharField(source='doctor_id.specialization.name')
    class Meta:
        model = Appointment
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionBill
        fields = '__all__'
#
# =========================================================================================
# =========================================================================================

class MedicinedetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDetails
        fields = '__all__'


class MedicinebillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineBill
        fields = '__all__'



# ===========================================================================================
#==========================================================================================
from .models import LabTestManagement, LabBill, LabReport
class LabtestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestManagement
        fields = '__all__'

class LabbillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabBill
        fields = '__all__'


class LabreportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabReport
        fields = '__all__'

#
# ==========================================================
# ==========================================================
from .models import MedicineHistory
class MedprescripSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicinePrescription
        fields = '__all__'

class MedicineHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineHistory
        fields = '__all__'
