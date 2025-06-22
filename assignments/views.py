

from django.shortcuts import render

def assignments(request):
    return render(request, 'assignments.html')

def upload(request):
    return render(request, 'assignment3.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def assignment_list(request):
    # your view logic here
    return render(request, 'assignments/list.html')
