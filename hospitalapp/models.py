from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name    = models.CharField(max_length=100)
    dep_details= models.TextField()
    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    Doctor_name=models.CharField(max_length=50)
    Doctor_special=models.CharField(max_length=50)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    Doctor_img=models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.Doctor_name

class Booking(models.Model):
    Patient_name=models.CharField(max_length=100)
    Phone_number=models.CharField(max_length=100)
    Email_id=models.EmailField()
    Doctor_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    Booing_date=models.DateField()
    Booked_on=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Patient_name