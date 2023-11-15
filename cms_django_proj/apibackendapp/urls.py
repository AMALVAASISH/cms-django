from django.urls import path
from .views import medicine_prescrip

urlpatterns = [
    path('medpre/',medicine_prescrip),
    # Add more URLs for other views/APIs as needed
]
