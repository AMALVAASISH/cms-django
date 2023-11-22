from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Staff, Doctor, Department, Specialization, Gender, BloodGroup, Receptionbill, Appointment, Patient, \
    MedicineBill, MedicineDetails, Quantity, PrescriptionDetail, Medicine
from rest_framework.parsers import JSONParser
from .serializers import GenderSerializer, BloodgroupSerializer, PatientSerializer, AppointmentSerializer, \
    BillSerializer, DoctorSerializer, StaffSerializer, DepartmentSerializer, SpecialisationSerializer, \
    QuantitySerializer, PrescriptionDetailSerializer, MedicineBillSerializers, MedicineSerializers, LabReportSerializer


def staff_list(request):
    if request.method == 'GET':
        staff_list = Staff.objects.all()
        serialized_staff_list = StaffSerializer(staff_list,many=True).data
        return JsonResponse(serialized_staff_list,safe=False,status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_staff = StaffSerializer(data=data)
        if serializer_add_staff.is_valid():
            serializer_add_staff.save()
            return JsonResponse(serializer_add_staff.data, status=201)
        return JsonResponse(serializer_add_staff.errors, status=400)

@csrf_exempt
def Staff_detail(request, id):
    try:
        staff = Staff.objects.get(id=id)
    except Staff.DoesNotExist:
        return JsonResponse({'error': 'Staff not found'}, status=404)

    if request.method == 'GET':
        serialized_staff = StaffSerializer(staff).data
        return JsonResponse(serialized_staff, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StaffSerializer(staff, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        staff.delete()
        return JsonResponse({'message': 'Satff deleted successfully'}, status=204)

def department_list(request):
    if request.method == 'GET':
        department_list = Department.objects.all()
        serialized_department_list = DepartmentSerializer(department_list,many=True).data
        return JsonResponse(serialized_department_list,safe=False,status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_department = DepartmentSerializer(data=data)
        if serializer_add_department.is_valid():
            serializer_add_department.save()
            return JsonResponse(serializer_add_department.data, status=201)
        return JsonResponse(serializer_add_department.errors, status=400)

@csrf_exempt
def department_detail(request, id):
    try:
        department = Department.objects.get(id=id)
    except Staff.DoesNotExist:
        return JsonResponse({'error': 'Department not found'}, status=404)

    if request.method == 'GET':
        serialized_Department = StaffSerializer(department).data
        return JsonResponse(serialized_Department, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(department, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        department.delete()
        return JsonResponse({'message': 'Department deleted successfully'}, status=204)

def specialisation_list(request):
    if request.method == 'GET':
        specialisation_list = Specialization.objects.all()
        serialized_specialisation_list = SpecialisationSerializer(specialisation_list,many=True).data
        return JsonResponse(serialized_specialisation_list,safe=False,status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_specialisation = SpecialisationSerializer(data=data)
        if serializer_add_specialisation.is_valid():
            serializer_add_specialisation.save()
            return JsonResponse(serializer_add_specialisation.data, status=201)
        return JsonResponse(serializer_add_specialisation.errors, status=400)

@csrf_exempt
def specialisation_detail(request, id):
    try:
        specialisation = Specialization.objects.get(id=id)
    except Specialization.DoesNotExist:
        return JsonResponse({'error': 'Specialization not found'}, status=404)

    if request.method == 'GET':
        serialized_Specialization = SpecialisationSerializer(specialisation).data
        return JsonResponse(serialized_Specialization, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SpecialisationSerializer(specialisation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        specialisation.delete()
        return JsonResponse({'message': 'Specialization deleted successfully'}, status=204)

def medicines(request):

    if request.method =='GET':
        medicines = MedicineDetails.objects.all()
        serialized_medicines = MedicinedetailsSerializer(medicines, many=True).data
        return JsonResponse(serialized_medicines,safe=False,status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_medicine = MedicinedetailsSerializer(data=data)
        if serializer_add_medicine.is_valid():
            serializer_add_medicine.save()
            return JsonResponse(serializer_add_medicine.data, status=201)
        return JsonResponse(serializer_add_medicine.errors, status=400)

# def medicine_quantity(request):
#     if request.method =='GET':
#         medicines_quantity = Quantity.objects.all()
#         serialized_medicines_quantity = QuantitySerializer(medicines_quantity, many=True).data
#         return JsonResponse(serialized_medicines_quantity,safe=False,status=200)

def medicine_quantity(request):
    if request.method == 'GET':
        medicine_quantity = MedicineQuantity.objects.all()
        serialized_lab_tests_admin = MedicineQuantitySerializer(medicine_quantity, many=True).data
        return JsonResponse(serialized_lab_tests_admin,safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_test = MedicineQuantitySerializer(data=data)
        if serializer_add_test.is_valid():
            serializer_add_test.save()
            return JsonResponse(serializer_add_test.data, status=201)
        return JsonResponse(serializer_add_test.errors, status=400)


def medicine_detail(request, medicine_id):

    medicine = MedicineDetails.objects.get(medicine_id=medicine_id)


    if request.method == 'GET':
        serialized_medicine = MedicinedetailsSerializer(medicine).data
        return JsonResponse(serialized_medicine, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedicinedetailsSerializer(medicine, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        medicine.delete()
        return JsonResponse({'message': 'Medicine deleted successfully'}, status=204)

    # For POST method to update an existing medicine with specific ID


def lab_tests_admin(request):
    if request.method == 'GET':
        lab_tests_admin = LabTestManagement.objects.all()
        serialized_lab_tests_admin = LabtestSerializer(lab_tests_admin, many=True).data
        return JsonResponse(serialized_lab_tests_admin,safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_test = LabtestSerializer(data=data)
        if serializer_add_test.is_valid():
            serializer_add_test.save()
            return JsonResponse(serializer_add_test.data, status=201)
        return JsonResponse(serializer_add_test.errors, status=400)


# def lab_detail(request, test_id):
#
#     lab_test = LabTestManagement.objects.get(test_id=test_id)
#
#
#     if request.method == 'GET':
#         serialized_lab_test = LabtestSerializer(lab_test).data
#         return JsonResponse(serialized_lab_test, status=200)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = LabtestSerializer(lab_test, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         lab_test.delete()
#         return JsonResponse({'message': 'Test deleted successfully'}, status=204)
def lab_detail(request, test_id):

    lab_test = Test.objects.get(test_id=test_id)


    if request.method == 'GET':
        serialized_lab_test = TestSerializers(lab_test).data
        return JsonResponse(serialized_lab_test, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TestSerializers(lab_test, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lab_test.delete()
        return JsonResponse({'message': 'Test deleted successfully'}, status=204)


def report_list(request):
    if request.method == "GET":
        #fetch all the posts data save it in the query set
        posts_list =LabReport.objects.all()
        #serialize the  query set,many =true bcoz we are processing a list
        serialized_post_list = LabreportSerializer(posts_list,many=True)
        #return the serialized object as a json response
        return JsonResponse(serialized_post_list.data,safe=False,status=200)
    elif request.method == 'POST':
        requested_data = JSONParser().parse(request)
        # Using serializer to serialize the parsed JSON for creating a new LabReport
        lab_report_create_serializer = LabreportSerializer(data=requested_data)
        # If the serializer returned valid serialized data
        if lab_report_create_serializer.is_valid():
            lab_report_create_serializer.save()
            # Send back the response code and the copy of data added
            return JsonResponse(lab_report_create_serializer.data, status=201)  # 201 Created status code
        return JsonResponse(lab_report_create_serializer.errors, status=400)

def lab_report_details_view(request,passed_id):
    try:
        lab_report_details = LabReport.objects.get(report_id=passed_id)
    except LabReport.DoesNotExist:
        return JsonResponse({'error': 'LabReport not found'}, status=404)

    if request.method == "GET":
        # serialize the lab report details
        serialized_lab_report_details = LabReportSerializer(lab_report_details)
        # return the serialized object as a JSON response
        return JsonResponse(serialized_lab_report_details.data, safe=False, status=200)

#
# ======================================================================

def gender_list(request):
    if request.method == 'GET':
        gender_list = Gender.objects.all()
        serialized_gender_list = GenderSerializer(gender_list,many=True).data
        return JsonResponse(serialized_gender_list,safe=False, status=200)

def bloodgroup_list(request):
    if request.method == 'GET':
        bloodgroup_list = BloodGroup.objects.all()
        serialized_bloodgroup_list = BloodgroupSerializer(bloodgroup_list,many=True).data
        return JsonResponse(serialized_bloodgroup_list, safe=False, status=200)
@csrf_exempt
def patient_list(request):
    if request.method == 'GET':
        patient_list = Patient.objects.all()
        serialized_patient_list = PatientSerializer(patient_list, many=True).data
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
@csrf_exempt
def patient_details_view(request, passed_id):
    # Get the details of the post with id passed_id
    patient_details = Patient.objects.get(id=passed_id)
    if request.method == 'GET':
        serialized_patient_details = PatientSerializer(patient_details).data
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
        serialized_doctor_list = DoctorSerializer(doctor_list, many=True).data
        return JsonResponse(serialized_doctor_list,safe=False,status=200)

@csrf_exempt
def appointment_list(request):
    if request.method == 'GET':
        appointment_list = Appointment.objects.all()
        serialized_appointment_list = AppointmentSerializer(appointment_list, many=True).data
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
    # elif request.method == 'PUT':
    #     # get the data from the default parameter
    #     request_data = JSONParser().parse(request)
    #     # using a serializer serialize the parsed json
    #     appointment_add_serializer = AppointmentSerializer(data=request_data)
    #     # if the serailizer return a valid serialized data
    #     if appointment_add_serializer.is_valid():
    #         appointment_add_serializer.save()
    #         # send back the response code and thew copy of data added as json
    #         return JsonResponse(appointment_add_serializer.data , status=200)
    #
    #     return JsonResponse(appointment_add_serializer.errors, status=400)
@csrf_exempt
def patient_appointment_details_view(request, passed_id):
    # Get the details of the post with id passed_id
    patient_appointment_details = Appointment.objects.get(id=passed_id)
    if request.method == 'GET':
        serialized_patient_appointment_details = AppointmentSerializer(patient_appointment_details).data
        return JsonResponse(serialized_patient_appointment_details, safe=False, status=200)

    elif request.method == 'PUT':
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using a serializer serialize the parsed json
        patient_appointment_edit_serializer = AppointmentSerializer(patient_appointment_details,data=request_data)
        # if the serailizer return a valid serialized data
        if patient_appointment_edit_serializer.is_valid():
            patient_appointment_edit_serializer.save()
            # send back the response code and the copy of data added as json
            return JsonResponse(patient_appointment_edit_serializer.data , status=200)

        return JsonResponse(patient_appointment_edit_serializer.errors, status=400)

@csrf_exempt
def recep_bill_list(request):
    if request.method == 'GET':
        recep_bill_list = Receptionbill.objects.all()
        serialized_recep_bill_list = BillSerializer(recep_bill_list, many=True).data
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

@csrf_exempt
def recep_bill_detail(request,passed_id):
    if request.method == 'GET':
        recep_bill_list = Receptionbill.objects.get(bill_no = passed_id)
        serialized_recep_bill_list = BillSerializer(recep_bill_list).data
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
# from .serializers import MedicinedetailsSerializer,MedicinebillSerializer
# def medicine_list(request):
#     if request.method =='GET':
#         medicine_list = MedicineDetails.objects.all()
#         serialized_medicine_list = MedicinedetailsSerializer(medicine_list, many=True).data
#         return JsonResponse(serialized_medicine_list,safe=False,status=200)

def medicines(request):

    if request.method =='GET':
        medicines = Medicine.objects.all()
        serialized_medicines = MedicineSerializers(medicines, many=True).data
        return JsonResponse(serialized_medicines,safe=False,status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_medicine = MedicineSerializers(data=data)
        if serializer_add_medicine.is_valid():
            serializer_add_medicine.save()
            return JsonResponse(serializer_add_medicine.data, status=201)
        return JsonResponse(serializer_add_medicine.errors, status=400)

def medicine_detail(request, medicine_id):

    medicine = Medicine.objects.get(medicine_id=medicine_id)


    if request.method == 'GET':
        serialized_medicine = MedicineSerializers(medicine).data
        return JsonResponse(serialized_medicine, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedicineSerializers(medicine, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        medicine.delete()
        return JsonResponse({'message': 'Medicine deleted successfully'}, status=204)
#
# def medicine_bill(request):
#     if request.method == 'GET':
#         medicine_bill = MedicineBill.objects.all()
#         serialized_medicine_bill = MedicinebillSerializer(medicine_bill, many=True).data
#         return JsonResponse(serialized_medicine_bill,safe=False,status=200)
#     elif request.method == 'POST':
#         # get the data from the default parameter
#         request_data = JSONParser().parse(request)
#         # using a serializer serialize the parsed json
#         medicine_bill_add_serializer = MedicinebillSerializer(data=request_data)
#         # if the serailizer return a valid serialized data
#         if medicine_bill_add_serializer.is_valid():
#             medicine_bill_add_serializer.save()
#             # send back the response code and thew copy of data added as json
#             return JsonResponse(medicine_bill_add_serializer.data, status=201)
#
#         return JsonResponse(medicine_bill_add_serializer.errors, status=400)
def medicine_bill(request):
    if request.method == 'GET':
        medicine_bill = MedicineBill.objects.all()
        serialized_medicine_bill = MedicineBillSerializers(medicine_bill, many=True).data
        return JsonResponse(serialized_medicine_bill,safe=False,status=200)

def doctor_prescription(request):
    if request.method == 'GET':
        doctor_prescription = MedicinePrescription.objects.all()
        # serialized_medicine_prescrip = MedprescripSerializer(medicine_prescrip,many=True)
        # return JsonResponse(serialized_medicine_prescrip,safe=False,status=200)
        serialized_data = [prescription.serialize() for prescription in doctor_prescription]

        # Return serialized data as JSON response
        return JsonResponse(serialized_data.data, safe=False, encoder=DjangoJSONEncoder)

#
# ==========================================================================================
# ===========================================================================================
from .models import LabTestManagement, LabBill,LabReport
# from .serializers import LabtestSerializer,LabbillSerializer,LabreportSerializer
def lab_tests(request):
    if request.method == 'GET':
        lab_tests = LabTestManagement.objects.all()
        serialized_lab_tests = LabtestSerializer(lab_tests,many=True).data
        return JsonResponse(serialized_lab_tests,safe=False,status=200)


def lab_bill(request):
    if request.method == 'GET':
        lab_bill = LabBill.objects.all()
        serialized_lab_bill = LabbillSerializer(lab_bill,many=True).data
        return JsonResponse(serialized_lab_bill,safe=False,status=200)


def lab_report_details_view(request, passed_id):
    lab_report_details = LabReport.objects.get(status=passed_id)
    if request.method == "GET":
        # serialize the lab report details
        serialized_lab_report_details = LabreportSerializer(lab_report_details)
        # return the serialized object as a JSON response
        return JsonResponse(serialized_lab_report_details.data, safe=False, status=200)

    elif request.method == 'PUT':
        requested_data = JSONParser().parse(request)
        # using serializer to serialize the parsed JSON
        lab_report_edit_serializer = LabreportSerializer(lab_report_details, data=requested_data)
        # if the serializer returned valid serialized data
        if lab_report_edit_serializer.is_valid():
            lab_report_edit_serializer.save()
            # send back the response code and the copy of data added
            return JsonResponse(lab_report_edit_serializer.data, status=200)
        return JsonResponse(lab_report_edit_serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     lab_report_details.delete()
    #
    #     return HttpResponse(status=204)

#
# ===========================================================
# ===========================================================
from .models import MedicinePrescription
# from .serializers import MedprescripSerializer
# def medicine_prescrip(request):
#     if request.method == 'GET':
#         medicine_prescriptions = MedicinePrescription.objects.all()
#         # serialized_medicine_prescrip = MedprescripSerializer(medicine_prescrip,many=True)
#         # return JsonResponse(serialized_medicine_prescrip,safe=False,status=200)
#         serialized_data = [prescription.serialize() for prescription in medicine_prescriptions]
#
#         # Return serialized data as JSON response
#         return JsonResponse(serialized_data, safe=False, encoder=DjangoJSONEncoder)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer_prescrip_medicine = MedprescripSerializer(data=data)
#         if serializer_prescrip_medicine.is_valid():
#             serializer_prescrip_medicine.save()
#             return JsonResponse(serializer_prescrip_medicine.data, status=201)
#         return JsonResponse(serializer_prescrip_medicine.errors, status=400)

@csrf_exempt
def prescription_details(request):
    if request.method == 'GET':
        medicine_prescriptions = PrescriptionDetail.objects.all()
        serialized_medicine_prescrip = PrescriptionDetailSerializer(medicine_prescriptions, many=True)
        return JsonResponse(serialized_medicine_prescrip.data, safe=False, status=200)

    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer_add_medicine = PrescriptionDetailSerializer(data=request_data)
        if serializer_add_medicine.is_valid():
            serializer_add_medicine.save()
            return JsonResponse(serializer_add_medicine.data, status=201)
        return JsonResponse(serializer_add_medicine.errors, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

from .models import MedicineHistory
from .serializers import MedicineHistorySerializer
def medicine_history_view(request):

    if request.method =='GET':
        medicines = MedicineHistory.objects.all()
        serialized_medicines = MedicineHistorySerializer(medicines, many=True).data
        return JsonResponse(serialized_medicines,safe=False,status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer_add_medicine = MedicineHistorySerializer(data=data)
        if serializer_add_medicine.is_valid():
            serializer_add_medicine.save()
            return JsonResponse(serializer_add_medicine.data, status=201)
        return JsonResponse(serializer_add_medicine.errors, status=400)


def medicine_prescription_details_view(request, passed_id):
    # Get the details of the post with id passed_id
    medicine_details = MedicinePrescription.objects.get(id=passed_id)
    if request.method == 'GET':
        serialized_patient_details = MedprescripSerializer(medicine_details).data
        return JsonResponse(serialized_patient_details, safe=False, status=200)

    elif request.method == 'PUT':
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using a serializer serialize the parsed json
        patient_edit_serializer = MedicinePrescription(medicine_details,data=request_data)
        # if the serailizer return a valid serialized data
        if patient_edit_serializer.is_valid():
            patient_edit_serializer.save()
            # send back the response code and the copy of data added as json
            return JsonResponse(patient_edit_serializer.data , status=200)

        return JsonResponse(patient_edit_serializer.errors, status=400)

def medical_history_details_view(request, passed_id):
    # Get the details of the post with id passed_id
    medical_details = MedicineHistory.objects.get(id=passed_id)
    if request.method == 'GET':
        serialized_patient_details = MedicineHistorySerializer(medical_details).data
        return JsonResponse(serialized_patient_details, safe=False, status=200)

    elif request.method == 'PUT':
        # get the data from the default parameter
        request_data = JSONParser().parse(request)
        # using a serializer serialize the parsed json
        patient_edit_serializer = MedicineHistorySerializer(medical_details,data=request_data)
        # if the serailizer return a valid serialized data
        if patient_edit_serializer.is_valid():
            patient_edit_serializer.save()
            # send back the response code and the copy of data added as json
            return JsonResponse(patient_edit_serializer.data , status=200)

        return JsonResponse(patient_edit_serializer.errors, status=400)








































