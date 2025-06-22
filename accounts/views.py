from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Student  # Ensure this line is present

def signin(request):
    if request.method == 'POST':
        # The form sends the enrollment number using "username".
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # On successful login, redirect to the dashboard.
            return redirect('dashboard')
        else:
            # Show error message if credentials are invalid.
            return render(request, 'signin.html', {'error': 'Invalid credentials'})
    return render(request, 'signin.html')


# def registration(request):
#     if request.method == 'POST':
#         # Process your registration form data here and create a user.
#         # For example:
#         # user = User.objects.create_user(...)
#         # return redirect('signin')
#         pass
#     return render(request, 'registration.html')


# def registration(request):
#     if request.method == 'POST':
#         Student.objects.create(
#             full_name=request.POST.get('fullName'),
#             gender=request.POST.get('gender'),
#             date_of_birth=request.POST.get('dob'),
#             enrollment_number=request.POST.get('enrollment'),
#             mobile=request.POST.get('mobile'),
#             email=request.POST.get('email'),
#             password=request.POST.get('password')  # Reminder: This should be hashed!
#         )
#         # Redirect to the sign in page after successful registration
#         return redirect('signin')
#     return render(request, 'registration.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Student

def registration(request):
    if request.method == 'POST':
        # Extract data from the POST request.
        full_name = request.POST.get('fullName')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        enrollment = request.POST.get('enrollment')  # Enrollment number entered by the user.
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create a Django User record.
        # The enrollment number is used as the username.
        user = User.objects.create_user(
            username=enrollment,    # Enrollment number acts as username.
            email=email,
            password=password       # create_user() automatically hashes the password.
        )
        # Optionally, store the user's full name in the User model.
        # If you have separate first_name/last_name fields, you can parse them; here we set full name as first_name.
        user.first_name = full_name
        user.save()

        # Create a Student profile, if you keep additional details in a separate custom model.
        # Either save the user password (which is hashed) or simply reference the created Django User.
        Student.objects.create(
            full_name=full_name,
            gender=gender,
            date_of_birth=dob,
            enrollment_number=enrollment,
            mobile=mobile,
            email=email,
            password=user.password  # The hashed password from the User record.
        )
        # Redirect to the sign in page after successful registration.
        return redirect('signin')
    return render(request, 'registration.html')

# @login_required
@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'dashboard.html')

# def logout(request):
#     logout(request)
#     return redirect('signin')


def signout(request):
    logout(request)  # Calls Django's logout function
    return redirect('signin')

# from django.shortcuts import render

# def dashboard(request):
#     return render(request, 'dashbord.html')

# def registration(request):
#     return render(request, "registration.html")

# def signin(request):
#     return render(request, "signin.html")
