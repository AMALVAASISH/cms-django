from django.urls import path
from .views import medicine_prescrip, patient_list, patient_details_view, doctor_list, appointment_list, \
    recep_bill_list, staff_list, Staff_detail, department_list, department_detail, specialisation_list, \
    specialisation_detail, medicine_list, lab_tests, medicines, medicine_detail, lab_tests_admin, lab_detail, patient_appointment_details_view,recep_bill_detail,lab_bill

urlpatterns = [
    path('medpre/',medicine_prescrip),
    path('api/patients/',patient_list),
    path('api/patients/<int:passed_id>', patient_details_view),
    path('api/doctors/',doctor_list),
    path('api/appointments/',appointment_list),
    path('api/appointments/<int:passed_id>', patient_appointment_details_view),
    path('api/receptionbills/', recep_bill_list),
    path('api/receptionbills/<int:passed_id>/', recep_bill_detail),
    path('API/staff/', staff_list),
    path('API/staff/<int:id>/', Staff_detail),
    path('API/dept/', department_list),
    path('API/dept/<int:id>/', department_detail),
    path('API/spez/', specialisation_list),
    path('API/spez/<int:id>/', specialisation_detail),
    path('API/med/', medicine_list),
    path('API/labtest/', lab_tests),
    path('API/meds/', medicines),
    path('API/meds/<int:medicine_id>/', medicine_detail),
    path('API/labs/', lab_tests_admin),
    path('API/add/<int:test_id>/', lab_detail),
    path('API/medicines', medicines),
    path('API/labbill/',lab_bill)
    # Add more URLs for other views/APIs as needed
]
