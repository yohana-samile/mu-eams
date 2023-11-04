from django.contrib import messages
# from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# forms
from .forms import FormDepertment, FormUnit, FormYearOFStudy, FormProgramme, FormEducationLevel, FormSemester, FormCourse, StudentForm,  UserStaffForm
# for fetching data
from eams.models import Department, Unit, Year_of_study, Programme, Education_level, Semester, Course, Student, Staff

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message = "Wrong username or password"
            messages.error(request, error_message)
            return redirect('index')
    return render(request, 'authentication/login.html')

# logout
def logout_view(request):
    logout(request)
    return redirect("authentication:login")

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

# staff data
def staff(request):
    return render(request, 'user/staff.html')

# units
def unit(request):
    if request.method == "POST":
        form = FormUnit(request.POST or None)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, "Success: Unit Added Successfully")
            return redirect('unit')
        else:
            messages.error(request, "Somethong went wrong, please try again")
            return redirect('unit')
    else:
        form = FormUnit()
        all_unit = Unit.objects.all()
        data = { 
           'units':all_unit
        }
    return render(request, 'unit/unit.html', data)


# depertment
def depertment(request):
    if request.method == 'POST':
        formOfDep = FormDepertment(request.POST or None)
        if formOfDep.is_valid():
            formOfDep.save()
            messages.add_message(request, messages.INFO, "Success: Depertment Added Successfully")
            return redirect('depertment')

        else:
            messages.error(request, "Something Went Wrong Try Again")
            return redirect('depertment')

    # else:
    formOfDep = FormDepertment()    
    all_dep = Department.objects.all()
    all_unit = Unit.objects.all()
    context = {
        'depertments': all_dep,
        'units':all_unit,
    }
    return render(request, 'depertment/depertment.html', context)

# year_of_study
def year_of_study(request):
    if request.method == "POST":
        form = FormYearOFStudy(request.POST or None)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.INFO, "Success: Year Added Successfully")
            return redirect('year_of_study')
        else:
            messages.error(request, "Somethong went wrong, please try again")
            return redirect('year_of_study')
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
            return redirect('programme')
        else:
            messages.add_message(request, messages.ERROR, "Somethong went wrong, please try again")
            return redirect('programme')
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
            return redirect('education_level')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong, Please try again.")
            return redirect('education_level')
        
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
            return redirect('semester')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong, Please try again.")
            return redirect('semester')
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
            return redirect('course')
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong, Please try again.")
            return redirect('course')
    else:
        form = FormCourse()
        context = {
            'form':form,
            'semesters': Semester.objects.all(),
            'courses': Course.objects.all()
        }
    return render(request, 'course/course.html', context)


# student
def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # get_form = form.save(commit=False)
            # get_dept = Department.objects.get(id=int(request.POST['department']))
            # get_form.depertment = get_dept
            # get_form.save()
            student_user = form.save(commit=False)
            student_user.set_password('password')
            student_user.save()

            messages.add_message(request, messages.INFO, "Success, New Student Registred Successfully")
            return redirect('student')
        else:
            # print(request.POST['department'])
            messages.add_message(request, messages.ERROR, "Something went wrong, Please try again.")
            # print(form.errors)
            return redirect('student')
    
    form = StudentForm()
    context = {
        'form':form,
        'all_dep': Department.objects.all(),
        'all_prog': Programme.objects.all(),
        'students': Student.objects.all(),
    }

    return render(request, 'user/student.html', context)

# UserStaffForm
def staff(request):
    if request.method == "POST":
        form = UserStaffForm(request.POST)
        if form.is_valid():
            # rol_number = form.cleaned_data['rol_number']
            # email = form.cleaned_data['email']
            # if Staff.objects.filter(rol_number=rol_number).exists() or Staff.objects.filter(email=email).exists():
            #     error = "Error, Staff User Exit"
            #     # messages.success(request, "Error, Staff User Exit")
            #     return render(request,'user/staff.html', error)

            # else:
            staff_user = form.save(commit=True)

            staff_user.set_password('password')
            staff_user.save()
            messages.success(request, "Success, New Staff User Registered Successfully")
            return redirect('staff')
        else:
            messages.error(request, "Something went wrong, Please try again.")
    else:
        form = UserStaffForm()
        context = {
            'form': form,
            'all_staff': Staff.objects.all(),
            'all_unit': Unit.objects.all(),
            'all_prog': Programme.objects.all(),
        }
    return render(request,'user/staff.html', context)
