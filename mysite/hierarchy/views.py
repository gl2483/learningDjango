from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Employee, Department

def index(request):
    depts = Department.objects.all()
    context = {'depts': depts}
    return render(request, 'hierarchy/index.html', context)

def employeedetail(request, empolyee_id):
    return HttpResponse("You're looking at question %s." % empolyee_id)

def departmentdetail(request, department_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % department_id)

def adddept(request):
    input_name = request.POST['dept_name']
    d = Department(dept_name=input_name)
    d.save()
    return HttpResponseRedirect('hierarchy:index')
