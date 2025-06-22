
from django.shortcuts import render

def settings(request):
    return render(request, 'setting4.html')

def profile(request):
    return render(request,'profile.html')