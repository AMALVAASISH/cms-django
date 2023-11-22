from rest_framework import serializers
from .models import Doctor, Department, Staff, Specialization, User, Appointment, Patient, Receptionbill, Gender, \
    BloodGroup, MedicineBill, MedicineQuantity, Medicine, Test, PrescriptionDetail, MedicineHistory, LabBill, LabReport
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
    doctor_name = serializers.CharField(source='staff.name', read_only=True)
    specialisation = serializers.CharField(source='specialization', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
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
    patient_id = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        # exclude = ('patient_id',)
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor_id.staff.name', read_only=True)
    specialisation = serializers.CharField(source='doctor_id.specialization.name',read_only=True)
    appointment_id = serializers.ReadOnlyField()
    token_no = serializers.ReadOnlyField()
    class Meta:
        model = Appointment
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    bill_amount = serializers.ReadOnlyField()
    bill_no = serializers.ReadOnlyField()
    doctor_name = serializers.CharField(source='doctor_id.staff.name', read_only=True)
    class Meta:
        model = Receptionbill
        fields = '__all__'
#
# =========================================================================================
# =========================================================================================

# class MedicinedetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicineDetails
#         fields = '__all__'

class MedicineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '_all_'

# class MedicinebillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicineBill
#         fields = '__all__'



# ===========================================================================================
#==========================================================================================
# from .models import LabTestManagement, LabBill, LabReport
# class LabtestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabTestManagement
#         fields = '__all__'
#
# class LabbillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabBill
#         fields = '__all__'
#
#
# class LabreportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LabReport
#         fields = '__all__'
#
# #
# # ==========================================================
# # ==========================================================
# from .models import MedicineHistory
# class MedprescripSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicinePrescription
#         fields = '__all__'
#
# class MedicineHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MedicineHistory
#         fields = '__all__'

class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '_all_'


class MedicineQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineQuantity
        fields = ['quantity']


class PrescriptionDetailSerializer(serializers.ModelSerializer):
    medicine = serializers.ReadOnlyField()

    medicine_per_price = serializers.DecimalField(source='medicine.price_per_unit', read_only=True, max_digits=10,
                                                  decimal_places=2)
    medicine_name = serializers.CharField(source='medicine.medicine_name', read_only=True)
    medicine_quantity = MedicineQuantitySerializer(many=True, read_only=True, source='medicine_quantities')

    class Meta:
        model = PrescriptionDetail
        fields = ['id', 'medicine', 'medicine_prescription', 'medicine_name', 'dosage', 'time_of_consumption', 'days',
                  'medicine_per_price', 'medicine_quantity']


class MedicineHistorySerializer(serializers.ModelSerializer):
    choose_test = serializers.SerializerMethodField()
    patient_name = serializers.CharField(source='patient.fullname', read_only=True)
    doctor_name = serializers.CharField(source='doctor.staff.name', read_only=True)
    prescription_detai = PrescriptionDetailSerializer(many=True, source='prescription_details', read_only=True)

    class Meta:
        model = MedicineHistory
        fields = ['id', 'patient', 'doctor','doctor_name','patient_name', 'dateofvisit', 'observation_details', 'diagnosis_details', 'choose_test',
                  'prescription_detai']

    def get_choose_test(self, obj):
        return [test.name for test in obj.choose_test.all()]

class MedicineBillSerializers(serializers.ModelSerializer):
    staff_name = serializers.CharField(source='staff_id.name', read_only=True)
    patient_name = serializers.CharField(source='patient_id.fullname', read_only=True)
    medicine_prescription_id = serializers.SerializerMethodField()

    class Meta:
        model = MedicineBill
        fields = ['staff_name', 'patient_name', 'medicine_prescription_id', 'price', 'date', 'medicine_bill_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    def get_medicine_prescription_id(self, obj):
        medicine_prescription = obj.medicine_prescription_id
        if medicine_prescription:
            return {
                'medicines': [
                    {
                        'name': detail.medicine.medicine_name,
                        'dosage': detail.dosage,
                        'time_of_consumption': detail.time_of_consumption,
                        'quantity': self.get_quantity(detail)
                    }
                    for detail in medicine_prescription.prescription_details.all()
                ]
            }
        return None

    def get_quantity(self, detail):
        medicine_quantity = MedicineQuantity.objects.filter(prescribed_medicine=detail).first()
        if medicine_quantity:
            return medicine_quantity.quantity
        return 1  # Default quantity if not found


class LabBillSerializer(serializers.ModelSerializer):
    patient_id = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()  # Use SerializerMethodField instead of DoctorSerializers
    tested_tests = serializers.SerializerMethodField()

    class Meta:
        model = LabBill
        fields = ('id', 'patient_id', 'doctor', 'tested_tests', 'total_price', 'test_bill_id', 'staff_id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    def get_patient_id(self, obj):
        patient = obj.patient_id
        return {'id': patient.id, 'fullname': patient.fullname}

    def get_doctor(self, obj):
        doctor_availability = obj.doctor_id
        doctor = doctor_availability.doctor if isinstance(doctor_availability,
                                                          Doctor) else doctor_availability
        return {'doctor_name': doctor.staff.name}

    def get_tested_tests(self, obj):
        tested_tests = obj.tested_tests
        return {
            'given-tests': [{'name': test.name, 'price': test.price}
                            for test in tested_tests.choose_test.all()]
        }


class LabReportSerializer(serializers.ModelSerializer):
    staff = serializers.CharField(source='staff_id.name', read_only=True)
    patient_name = serializers.CharField(source='patient_id.fullname', read_only=True)
    doctor_name = serializers.CharField(source='doctor_id.doctor.staff.name', read_only=True)
    tests_info = serializers.SerializerMethodField(read_only=True)

    def get_tests_info(self, obj):
        # Assuming 'tests' is a ManyToManyField in your LabReport model
        tests = obj.tests.all()
        return [{'name': test.name, 'price': test.price} for test in tests]

    class Meta:
        model = LabReport
        fields = (
        'id', 'staff_id', 'doctor_id', 'patient_id', 'tests', 'patient_name', 'doctor_name', 'staff', 'report',
        'lab_report_id', 'test_bill_id', 'tests_info')
        read_only_fields = ('lab_report_id',)
