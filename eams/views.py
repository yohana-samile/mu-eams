from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from django.db.models import Sum
from .forms import FormDepertment, FormUnit, FormYearOFStudy, FormProgramme, FormEducationLevel, FormSemester, FormCourse, StudentForm, SemesterRegistrationForm, Payment_for_Student, StaffForm
# for fetching data
from eams.models import Department, Unit, Year_of_study, Programme, Education_level, Semester, Course, Student, SemesterRegistration, Payment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import random

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # end semester
            current_Semester = Semester.objects.filter(semester_end_at__lte=timezone.now()).first()
            if current_Semester and current_Semester.status == 'continuing':
                current_Semester.status = 'end'
                current_Semester.save()
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
# @login_required(login_url="authentication/../")
def footer1(request):
    return render(request, 'layout/footer1.html')

# @login_required(login_url="authentication/../")
def layout(request):
    user = request.user
    student_regstraion = SemesterRegistration.objects.filter(semester_registration_status='regstered', user=request.user).first()
    student = {
        'user': user,
        'student_regstraion': student_regstraion
    }
    return render(request, 'layout/layout.html', student)

# @login_required(login_url="authentication/../")
def home(request):
    return render(request, 'home.html')

# units
# @login_required(login_url="authentication/../")
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
# @login_required(login_url="authentication/../")
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
# @login_required(login_url="authentication/../")
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
# @login_required(login_url="authentication/../")
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
# @login_required(login_url="authentication/../")
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
# @login_required(login_url="authentication/../")
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
            'semesters': Semester.objects.order_by('-created_at')
        }
    return render(request, 'semester/semester.html', context)

# course
# @login_required(login_url="authentication/../")
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

from django.contrib.auth import get_user_model
# student
# @login_required(login_url="authentication/../")
def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            localvar = form.save(commit=False)
            user = get_user_model().objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            localvar.user = user
            localvar.save()
            messages.add_message(request, messages.INFO, "Success, New Student Registred Successfully")
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong, Please try again.")
    
    form = StudentForm()
    context = {
        'form':form,
        'all_dep': Department.objects.all(),
        'all_prog': Programme.objects.all(),
        'students': Student.objects.all(),
        # 'students': Student.objects.filter(student__isnull=False).values(
        #     'first_name', 'last_name', 'email', 'username', 'programme'
        # mumsaco1_mumsa pass mumsa1234567890mumsa
        # email mumsa@mumsa.co.tz pass mumsa1234567890mumsa
        # ),
    }
    return render(request, 'user/student.html', context)

# staff data
# @login_required(login_url="authentication/../")
def staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            register_staff = form.save(commit=False)
            user = get_user_model().objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
            )
            register_staff.user = user
            register_staff.save()
            messages.add_message(request, messages.INFO, "Success, New Staff Registred Successfully")
        else:
            messages.add_message(request, messages.ERROR, "Something went wrong, Please try again.")
    form = StaffForm()
    context = {
        'form':form,
        'all_dep': Department.objects.all(),
        'students': Student.objects.all(),
    }
    return render(request, 'user/staff.html', context)

# user profile
# @login_required(login_url='authentication/../')
def profile(request):
    user = request.user
    return render(request, 'profile/user_profile.html', {'user': user})

# student_semester_registration
def student_semester_registration(request):
    if request.method == "POST":
        form = SemesterRegistrationForm(request.POST)
        if form.is_valid():
            semester_registration = form.save(commit=False)
            semester_registration.user = request.user
            semester_registration.save()

            messages.add_message(request, messages.INFO, "Success, Successfully Registered On This Semester")
            return redirect('student_semester_registration')

        else:
            messages.error(request, messages.INFO, "Something went wrong, Please try again.")    
    else:
        form = SemesterRegistrationForm
    user = request.user
    semester_registrations = SemesterRegistration.objects.filter(user=user)
    semesters = {
        'user_id': user,
        'all_semester': Semester.objects.all(),
        'student_semester_registration': semester_registrations,
    }
    return render(request, 'semester/student_semester_registration.html', semesters)
   
def programme_stracture(request):
    context = {
        'courses': Course.objects.all(),
        'years': Year_of_study.objects.all()
    }
    return render(request, 'programme/programme_stracture.html', context)

# register_my_course
def register_my_course(request):
    return render(request, 'course/register_my_course.html')

# exam_attendance, payment
def exam_attendance(request):
    return render(request, "exam/exam_attendance.html")

def payment(request):
    if request.method == "POST":
        form = Payment_for_Student(request.POST)
        if form.is_valid():
            receipt_number = random.randint(100000, 999999)
            student_payment = form.save(commit=False)
            student_payment.receipt = receipt_number
            student_payment.save()
            messages.add_message(request, messages.INFO, "Payment Complite")
            return redirect('payment')
        else:
            messages.error(request, messages.INFO, "Something went wrong, Please try again.")
    form = Payment_for_Student()
    user = request.user
    student = Student.objects.get(user=user)
    payments = Payment.objects.filter(student=student)
    total_paid = payments.aggregate(total_paid_amount=Sum('amount'))['total_paid_amount'] or 0

    context = {
        'user': user,
        'payments': payments,
        'total_paid': total_paid
    }
    return render(request, 'payment/payment.html', context)
# logout
# def logout(request):
#     auth.logout(request)
#     return render('authentication/logout.html')
