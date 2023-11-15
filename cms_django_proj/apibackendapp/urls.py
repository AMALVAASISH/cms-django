from django.urls import path
from .views import medicine_prescrip, patient_list, patient_details_view, doctor_list,appointment_list,recep_bill_list

urlpatterns = [
    path('medpre/',medicine_prescrip),
    path('api/patients/',patient_list),
    path('api/patients/<int:passed_id>/', patient_details_view),
    path('api/doctors/',doctor_list),
    path('api/appointments/',appointment_list),
    path('api/receptionbills/', recep_bill_list),

    # Add more URLs for other views/APIs as needed
]
