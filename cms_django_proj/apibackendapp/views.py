from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views import View
from .models import Staff, Doctor, Department, Specialization,Gender,BloodGroup,ReceptionBill,Appointment,Patient, MedicineBill,MedicineDetails
from rest_framework.parsers import JSONParser
from .serializers import GenderSerializer,BloodgroupSerializer, PatientSerializer,AppointmentSerializer,BillSerializer,DoctorSerializer,StaffSerializer,DepartmentSerializer,SpecialisationSerializer

def staff_list(request):
    if request.method == 'GET':
        staff_list = Staff.objects.all()
        serialized_staff_list = StaffSerializer(staff_list,many=True)
        return JsonResponse(serialized_staff_list,safe=False,status=200)

def department_list(request):
    if request.method == 'GET':
        department_list = Department.objects.all()
        serialized_department_list = DepartmentSerializer(staff_list,many=True)
        return JsonResponse(serialized_department_list,safe=False,status=200)

def specialisation_list(request):
    if request.method == 'GET':
        specialisation_list = Specialization.objects.all()
        serialized_specialisation_list = StaffSerializer(staff_list,many=True)
        return JsonResponse(serialized_specialisation_list,safe=False,status=200)
#
# ======================================================================

def gender_list(request):
    if request.method == 'GET':
        gender_list = Gender.objects.all()
        serialized_gender_list = GenderSerializer(gender_list,many=True)
        return JsonResponse(serialized_gender_list,safe=False, status=200)

def bloodgroup_list(request):
    if request.method == 'GET':
        bloodgroup_list = BloodGroup.objects.all()
        serialized_bloodgroup_list = BloodgroupSerializer(bloodgroup_list,many=True)
        return JsonResponse(serialized_bloodgroup_list, safe=False, status=200)

def patient_list(request):
    if request.method == 'GET':
        patient_list = Patient.objects.all()
        serialized_patient_list = PatientSerializer(patient_list, many=True)
        return JsonResponse(serialized_patient_list,safe=False,status=200)

    elif request.method == 'POST':
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using a serializer serialize the parsed json
        patient_add_serializer = PatientSerializer(data=request_data)
        # if the serailizer return a valid serialized data
        if patient_add_serializer.is_valid():
            patient_add_serializer.save()
            # send back the response code and thew copy of data added as json
            return JsonResponse(patient_add_serializer.data , status=201)

        return JsonResponse(patient_add_serializer.errors, status=400)

def patient_details_view(request, passed_id):
    # Get the details of the post with id passed_id
    patient_details = Patient.objects.get(id=passed_id)
    if request.method == 'GET':
        serialized_patient_details = PatientSerializer(patient_details, many=True)
        return JsonResponse(serialized_patient_details, safe=False, status=200)

    elif request.method == 'PUT':
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using a serializer serialize the parsed json
        patient_edit_serializer = PatientSerializer(patient_details,data=request_data)
        # if the serailizer return a valid serialized data
        if patient_edit_serializer.is_valid():
            patient_edit_serializer.save()
            # send back the response code and the copy of data added as json
            return JsonResponse(patient_edit_serializer.data , status=200)

        return JsonResponse(patient_edit_serializer.errors, status=400)


def doctor_list(request):
    if request.method == 'GET':
        doctor_list = Doctor.objects.all()
        serialized_doctor_list = DoctorSerializer(doctor_list, many=True)
        return JsonResponse(serialized_doctor_list,safe=False,status=200)

def appointment_list(request):
    if request.method == 'GET':
        appointment_list = Appointment.objects.all()
        serialized_appointment_list = AppointmentSerializer(appointment_list, many=True)
        return JsonResponse(serialized_appointment_list,safe=False,status=200)

    elif request.method == 'POST':
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using a serializer serialize the parsed json
        appointment_add_serializer = AppointmentSerializer(data=request_data)
        # if the serailizer return a valid serialized data
        if appointment_add_serializer.is_valid():
            appointment_add_serializer.save()
            # send back the response code and thew copy of data added as json
            return JsonResponse(appointment_add_serializer.data , status=201)

        return JsonResponse(appointment_add_serializer.errors, status=400)


def recep_bill_list(request):
    if request.method == 'GET':
        recep_bill_list = ReceptionBill.objects.all()
        serialized_recep_bill_list = BillSerializer(recep_bill_list, many=True)
        return JsonResponse(serialized_recep_bill_list,safe=False,status=200)

    elif request.method == 'POST':
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using a serializer serialize the parsed json
        recep_bill_add_serializer = BillSerializer(data=request_data)
        # if the serailizer return a valid serialized data
        if recep_bill_add_serializer.is_valid():
            recep_bill_add_serializer.save()
            # send back the response code and thew copy of data added as json
            return JsonResponse(recep_bill_add_serializer.data , status=201)

        return JsonResponse(recep_bill_add_serializer.errors, status=400)

# ====================================================================================
# =====================================================================================
from .serializers import MedicinedetailsSerializer,MedicinebillSerializer
def medicine_list(request):
    if request.method =='GET':
        medicine_list = MedicineDetails.objects.all()
        serialized_medicine_list = MedicinedetailsSerializer(medicine_list, many=True)
        return JsonResponse(serialized_medicine_list,safe=False,status=200)


def medicine_bill(request):
    if request.method == 'GET':
        medicine_bill = MedicineBill.objects.all()
        serialized_medicine_bill = MedicinebillSerializer(medicine_bill, many=True)
        return JsonResponse(serialized_medicine_bill,safe=False,status=200)

#
# ==========================================================================================
# ===========================================================================================
from .models import LabTestManagement, LabBill
from .serializers import LabtestSerializer,LabbillSerializer,LabreportSerializer
def lab_tests(request):
    if request.method == 'GET':
        lab_tests = LabTestManagement.objects.all()
        serialized_lab_tests = LabtestSerializer(lab_tests,many=True)
        return JsonResponse(serialized_lab_tests,safe=False,status=200)


def lab_bill(request):
    if request.method == 'GET':
        lab_bill = LabBill.objects.all()
        serialized_lab_bill = LabbillSerializer(lab_bill,many=True)
        return JsonResponse(serialized_lab_bill,safe=False,status=200)
#
# ===========================================================
# ===========================================================
from .models import MedicinePrescription
from .serializers import MedprescripSerializer
def medicine_prescrip(request):
    if request.method == 'GET':
        medicine_prescriptions = MedicinePrescription.objects.all()
        # serialized_medicine_prescrip = MedprescripSerializer(medicine_prescrip,many=True)
        # return JsonResponse(serialized_medicine_prescrip,safe=False,status=200)
        serialized_data = [prescription.serialize() for prescription in medicine_prescriptions]

        # Return serialized data as JSON response
        return JsonResponse(serialized_data, safe=False, encoder=DjangoJSONEncoder)













































