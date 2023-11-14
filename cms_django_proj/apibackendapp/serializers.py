from rest_framework import serializers
from .models import Doctor,Department,Staff,Specialization,User,Appointment,Patient,ReceptionBill

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionBill
        fields = '__all__'


