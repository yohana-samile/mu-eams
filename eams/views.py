from django.contrib import messages
# from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
# forms
from .forms import FormDepertment, FormUnit, FormYearOFStudy, FormProgramme, FormEducationLevel, FormSemester, FormCourse
# for fetching data
from eams.models import Department, Unit, Year_of_study, Programme, Education_level, Semester, Course

# Create your views here.
def index(request):
    return render(request, 'authentication/login.html')

def forgot_password(request):
    return render(request, 'authentication/forgot_password.html')

def header(request):
    return render(request, 'resource/header.html')

def footer(request):
    return render(request, 'resource/footer.html')


# protected view
def footer1(request):
    return render(request, 'layout/footer1.html')

def layout(request):
    return render(request, 'layout/layout.html')

def home(request):
    return render(request, 'home.html')

def student(request):
    return render(request, "user/student.html")

# staff data
def staff(request):
    return render(request, 'user/staff.html')

# depertment
def depertment(request):
    if request.method == 'POST':
        form = FormDepertment(request.POST or None)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, "Success: Depertment Added Successfully")
            return render(request, 'depertment/depertment.html')

        else:
            messages.error(request, "Something Went Wrong Try Again")
            return render(request, 'depertment/depertment.html')

    else:
        form = FormDepertment()    
        all_depertment = Department.objects.all()
        context = { 'depertments':all_depertment }
    return render(request, 'depertment/depertment.html', context)

# units
def unit(request):
    if request.method == "POST":
        form = FormUnit(request.POST or None)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, "Success: Unit Added Successfully")
            return render(request, 'unit/unit.html')
        else:
            messages.error(request, "Somethong went wrong, please try again")
            return render(request, 'unit/unit.html')
    else:
        form = FormUnit()
        all_unit = Unit.objects.all()
        all_dep = Department.objects.all()

        data = { 'units':all_unit, 'dep':all_dep }
    return render(request, 'unit/unit.html', data)

# year_of_study
def year_of_study(request):
    if request.method == "POST":
        form = FormYearOFStudy(request.POST or None)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, "Success: Year Added Successfully")
            return render(request, "year_of_study/year_of_study.html")
        else:
            messages.error(request, "Somethong went wrong, please try again")
            return render(request, 'year_of_study/year_of_study.html')
    else:
        form = FormYearOFStudy()
        all_year = Year_of_study.objects.all()
        data = { 'years':all_year }
    return render(request, 'year_of_study/year_of_study.html', data)

# programme
def programme(request):
    if request.method == "POST":
        form = FormProgramme(request.POST or None)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, "Success: Programme Added Successfully")
            return render(request, "programme/programme.html")
        else:
            messages.error(request, "Somethong went wrong, please try again")
            return render(request, 'programme/programme.html')
    else:
        form = FormProgramme()
        context = {
            'form': form,
            'programmes': Programme.objects.all(),
            'years': Year_of_study.objects.all(),
            'departments': Department.objects.all(),
        }
    return render(request, "programme/programme.html", context)

# education_level
def education_level(request):
    if request.method == "POST":
        form = FormEducationLevel(request.POST or None)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, "Success, New Education Level Added")
            return render(request, "education_level/education_level.html")
        else:
            messages.add_message(request, messages.INFO, "Something went wrong, Please try again.")
            return render(request, 'education_level/education_level.html')
        
    else:
        form = FormEducationLevel()
        
        context = {
            'form':form,
            'education_levels': Education_level.objects.all()
        }
    return render(request, 'education_level/education_level.html', context)

# semester
def semester(request):
    if request.method == "POST":
        form = FormSemester(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Success, Semester Added")
            return render(request, 'semester/semester.html')
        else:
            messages.add_message(request, messages.INFO, "Something went wrong, Please try again.")
            return render(request, 'semester/semester.html')
    else:
        form = FormSemester()
        context = {
            'form':form,
            'semesters': Semester.objects.all()
        }
    return render(request, 'semester/semester.html', context)

# course
def course(request):
    if request.method == "POST":
        form = FormCourse(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Success, New Course Added Successfully")
            return render(request, 'course/course.html')
        else:
            messages.add_message(request, messages.INFO, "Something went wrong, Please try again.")
            return render(request, 'course/course.html')
    else:
        form = FormCourse()
        context = {
            'form':form,
            'semesters': Semester.objects.all(),
            'courses': Course.objects.all()
        }
    return render(request, 'course/course.html', context)
