from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BloodGroup(models.Model):
    title = models.CharField(max_length=5)
    slug = models.SlugField()
    def __str__(self):
        return self.title


class Gender(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField()
    def __str__(self):
        return self.title

class Patient(models.Model):
    patient_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField()
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.patient_id

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    ROLE_CHOICES = [
        ('Doctor', 'Doctor'),
        ('Lab Technician', 'Lab Technician'),
        ('Pharmacist', 'Pharmacist'),
        ('Receptionist', 'Receptionist'),
        # Add other roles as needed
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15)  # Assuming phone number format
    date_of_joining = models.DateField()
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='doctor',
                                 limit_choices_to={'role': 'Doctor'})
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, blank=True, null=True)
    consultationfees = models.PositiveIntegerField(default=None)

    def __str__(self):
        return self.staff.name


class Appointment(models.Model):
    appointment_id = models.CharField(max_length=10)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    appointment_date = models.DateField(auto_now_add=True)
    token_no = models.IntegerField()
    def __str__(self):
        return self.appointment_id

class ReceptionBill(models.Model):
    bill_no = models.IntegerField()
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bill_amount = models.IntegerField()
    bill_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.bill_no

class MedicineDetails(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=255,default=None)
    company_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.medicine_name


class MedicineBill(models.Model):
    bill_no = models.IntegerField(primary_key=True)
    medicine_prescription = models.ForeignKey('MedicinePrescription', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateField(auto_now_add=True)
    paying_status = models.BooleanField(default=False)
    staff_name = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.bill_no

class LabTestManagement(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255, unique=True, default=None)
    is_active = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.test_name


class LabBill(models.Model):
    bill_number = models.CharField(max_length=20, unique=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill - {self.bill_number}"


class LabReport(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    low_range = models.FloatField()
    high_range = models.FloatField()
    actual_value = models.FloatField()
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lab Report - {self.status}"


class MedicineHistory(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_of_visit = models.DateField()
    observation_details = models.TextField()
    diagnosis_details = models.TextField()
    def __str__(self):
        return str(self.id)

# class TestPrescription(models.Model):
#     id = models.AutoField(primary_key=True)
#     doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
#     patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     choose_test = models.ForeignKey(LabTestManagement, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.id

# class TestPrescriptionTests(models.Model):
#     id = models.AutoField(primary_key=True)
#     test_prescription_id = models.ForeignKey(TestPrescription, on_delete=models.CASCADE)
#     test_id = models.ManyToManyField(LabTestManagement)
#     def __str__(self):
#         return self.id

class MedicinePrescription(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine_id = models.ManyToManyField(MedicineDetails, blank=True)
    test_id = models.ManyToManyField(LabTestManagement, blank=True)
    dosage = models.CharField(max_length=255)
    time_of_consumption = models.CharField(max_length=255)
    duration = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

    def serialize(self):
        medicine_details_data = list(self.medicine_id.values('medicine_id', 'medicine_name', 'company_name', 'quantity', 'price_per_unit'))

        # Add dosage to each medicine_details entry
        for med_detail in medicine_details_data:
            med_detail['dosage'] = self.dosage

        lab_details_data = list(self.test_id.values('test_id', 'test_name', 'amount'))
        doctor_id = None
        if hasattr(self, 'doctor_id') and hasattr(self.doctor_id.staff, 'doctor_id'):
            doctor_id = self.doctor_id.staff.doctor_id
        return {
            'id': self.id,
            'patient_id': self.patient_id.patient_id,
            'doctor_id': doctor_id,
            'appointment_id': self.appointment_id.appointment_id,
            'medicine_details': medicine_details_data,
            'lab_test_details': lab_details_data,
            'dosage': self.dosage,
            'time_of_consumption': self.time_of_consumption,
            'duration': self.duration,
        }
class MedicinePrescriptionMedicines(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_prescription_id = models.ForeignKey(MedicinePrescription, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(MedicineDetails, on_delete=models.CASCADE)
    def __str__(self):
        return self.id


