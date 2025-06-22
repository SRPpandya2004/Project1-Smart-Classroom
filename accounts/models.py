

# Create your models here.
from django.db import models
from django.contrib import admin  # Correct import

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    enrollment_number = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Consider hashing this later

    def __str__(self):
        return self.full_name
    

#________________________MAnualy added_____________________________________
#__________________________________________________________________________



# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'enrollment_number', 'email', 'gender')
#     search_fields = ('full_name', 'enrollment_number', 'email')

# admin.site.register(Student, StudentAdmin)


