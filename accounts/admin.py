

# # accounts/admin.py
# from django.contrib import admin
# from .models import Student  # assuming you have a Student model

# admin.site.register(Student)

# admin.py
from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'enrollment_number', 'email', 'gender')
    search_fields = ('full_name', 'enrollment_number', 'email')

admin.site.register(Student, StudentAdmin)