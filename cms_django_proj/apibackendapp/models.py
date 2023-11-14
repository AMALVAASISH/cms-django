from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class bloodgroup(models.Model):
    title = models.CharField(max_length=5)
    slug = models.SlugField()

class gender(models.Model):
    title = models.CharField(max_length=15)
    slug = models.SlugField()
class Patient(models.Model):
    patientId = models.CharField(max_length=10)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dob = models.DateField()
    mobileno = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    bloodGroup = models.ForeignKey(bloodgroup, on_delete=models.CASCADE)
    gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)






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
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE, related_name='doctor')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.staff.name

class Appointment(models.Model):
    appointmentid = models.CharField(max_length=10)
    patientid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specializationid =  models.ForeignKey(Specialization,on_delete=models.CASCADE)
    appointmentdate = models.DateField(auto_now_add=True)
    Tokenno = models.IntegerField()

class Bill(models.Model):
    billno = models.IntegerField()
    appointmentid = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patientid = models.ForeignKey(Patient, on_delete=models.CASCADE)
    billamount = models.IntegerField()
    billdate = models.DateTimeField(auto_now_add=True)
