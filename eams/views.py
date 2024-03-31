from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from django.db.models import Sum

from eams.admin import User
from .forms import FormDepertment, FormUnit, FormYearOFStudy, FormProgramme, FormEducationLevel, FormSemester, FormCourse, StudentForm, SemesterRegistrationForm, Payment_for_Student, StaffForm, Exam_attendace_form, Biometric_data_form, Final_exam_attendence_record_form
# for fetching data
from eams.models import Department, Unit, Year_of_study, Programme, Education_level, Semester, Course, Student, SemesterRegistration, Payment, Staff, Student_course_work, Exam_attendace, Biometric_data, Final_exam_attendence_record
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import random
from django.db.models import F
from .utils import get_final_exam_attendence_record_model
from django.core.serializers import serialize


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
        'students': Student.objects.select_related('user').all(),
        'fingers': Biometric_data.objects.select_related('student').all(),
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
                last_name=request.POST['last_name'],
                is_staff=True
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
        'staffs': Staff.objects.all(),
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

# student_cw
def student_cw(request):
    user = request.user
    if request.method == "GET" and 'programme_id' in request.GET:
        programme_id = request.GET['programme_id']
        # Implement logic to retrieve students based on the selected program ID
        students = Student.objects.filter(programme_id=programme_id).select_related('programme')
        courses = Course.objects.all()    
        programmes = Programme.objects.all()

        students_data = [{'id': student.id, 'reg_number': student.reg_number, 'programme_abbrevation': student.programme.programme_abbrevation } for student in students]
        courses_data = [{'id': course.id, 'code': course.code} for course in courses]
        programmes_data = [{'id': programme.id, 'programme_abbrevation': programme.programme_abbrevation} for programme in programmes]

        context = {
            'user_id': user.id,
            'programmes': programmes_data,
            'courses': courses_data,
            'students': students_data
        }
        return JsonResponse(context, safe=False)
    
    # data submission
    elif request.method == "POST":
        course_work_value = request.POST.get('course_work_value')
        programme_id = request.POST.get('programme_id')
        student_id = request.POST.get('student_id')
        # for update cw value
        id = request.POST.get('id')
        # to update c_code to all students
        course = request.POST.get('course')
        programmeId = request.POST.get('programmeId')

        # check if cw submitted 
        student_course_work_instance, created = Student_course_work.objects.get_or_create(
            course_work_value = course_work_value,
            programme_id=programme_id,
            student_id=student_id,
        ) 
        student_course_work_instance.course_work_value = course_work_value
        
        # for update cw value
        if not created:
            student_course_work_instance.id = id
        
        # else:
        Student_course_work.objects.filter(programme_id=programmeId).update(course=course)
            # UPDATE `student_course_work` SET course ='css 111'
        student_course_work_instance.save()

        student_course_work = Student_course_work.objects.all()
        success = {
            'success': True,     
            'course_id': student_course_work_instance.id,
            'updateCw': course_work_value,
            'student_course_work': student_course_work
        }
        return JsonResponse(success)      
    else:
        context = {
            'programmes': Programme.objects.all(),
            'courses': Course.objects.all(),
        }
        template =  'cw/student_cw.html'
    return render(request, template, context)

# exam_attendance, payment
def exam_attendance(request):
    if request.method == "GET" and 'unit_id' in request.GET:
        unit_id = request.GET['unit_id']
        depertments = Department.objects.filter(unit_id=unit_id).values('id', 'name')
        return JsonResponse(list(depertments), safe=False)
        # get programme
    elif request.method == "GET" and 'department_id' in request.GET:
        department_id = request.GET['department_id']
        programmes = Programme.objects.filter(department_id=department_id).values('id', 'name')
        return JsonResponse(list(programmes), safe=False)
        # get course
    elif request.method == "GET" and 'semester_id' in request.GET:
        semester_id = request.GET['semester_id']
        all_courses = Course.objects.filter(semester_id=semester_id).values('id', 'name')
        submitted_course_ids = Exam_attendace.objects.filter(semester_id=semester_id).values_list('course_id', flat=True)
        unsubmitted_courses = all_courses.exclude(id__in=submitted_course_ids)
        return JsonResponse(list(unsubmitted_courses), safe=False)
    
    # student_who_can_attend
    elif request.method == "GET" and 'programme_id' in request.GET:
        programme_id = request.GET['programme_id']
        student_list = list(Student.objects.filter(programme_id=programme_id).values('reg_number'))
        return JsonResponse(student_list, safe=False)

    # finilize Exam_attendace submission by chech if fingerprint match
    elif request.method == 'GET' and 'reg_number' in request.GET:
        reg_number = request.GET.get('reg_number')
        try:
            student = Student.objects.get(reg_number=reg_number)
        except Student.DoesNotExist:
            return JsonResponse({'reg_number_exists': False, 'fingerprint_match': False})
        fingerprint_match_exists = Biometric_data.objects.filter(student=student).exists()
        return JsonResponse({'reg_number_exists': True, 'fingerprint_match': fingerprint_match_exists})

    #submt exm attendence record 
    elif request.method == "POST":
        operation = request.POST.get('operation')
        if operation == 'insert':
            form = Exam_attendace_form(request.POST or None)
            if form.is_valid():
                exam_attendance_step1 = form.save(commit=False)

                unit = request.POST.get('unit')
                depertment = request.POST.get('depertment')
                programme = request.POST.get('programme')
                semester = request.POST.get('semester')
                course = request.POST.get('course')

                # assgn values
                programme_instance = get_object_or_404(Programme, id=programme)
                course_instance = get_object_or_404(Course, id=course)
                semester_instance = get_object_or_404(Semester, id=semester)
                depertment_instance = get_object_or_404(Department, id=depertment)

                exam_attendance_step1.unit = unit
                exam_attendance_step1.department = depertment_instance
                exam_attendance_step1.programme = programme_instance
                exam_attendance_step1.semester = semester_instance
                exam_attendance_step1.course = course_instance
                exam_attendance_step1.save()

                # get exam attendance data
                success = {'success': True}
                return JsonResponse(success, safe=False)
            else:
                return JsonResponse({'success': False, 'error': form.errors}, safe=False)
        # update
        elif operation == 'update':
            try:
                id = int(request.POST.get('id'))
                existing_record = get_object_or_404(Exam_attendace, id=id)
                existing_record.exam_status = request.POST.get('exam_status')
                existing_record.save()
                return JsonResponse({'success': True}, safe=False)
            except Exception as e:
                return JsonResponse({'success': False}, safe=False)
            
        # finilize Exam_attendace submission
        elif operation == "submit_student_who_attende_exam":
            reg_number = request.POST.get('reg_number')
            booklet_number = request.POST.get('booklet_number')
            signin_flag = request.POST.get('signin_flag') == 'on'
            signout_flag = request.POST.get('signout_flag') == 'on'
            # biometric_data = request.POST.get('biometric_data')
            biometric_data = 1
            
            try:
                student = Student.objects.get(reg_number=reg_number)
            except Student.DoesNotExist:
                return JsonResponse({'success': False, 'error_message': 'Student not found.'}, safe=False)
            
            fingerprint_match_exists = Biometric_data.objects.get(fingerprint=biometric_data)
            if fingerprint_match_exists:
                student = Student.objects.get(reg_number=reg_number)
                student_programme = student.programme_id
                if student_programme is not None:
                    programme_id_value = student_programme
                    exam_attend = Exam_attendace.objects.filter(programme_id=programme_id_value).first()
                    if exam_attend is not None:
                        exam_attend_id_value = exam_attend
                        biometry = fingerprint_match_exists
                        attendance, created = Final_exam_attendence_record.objects.get_or_create(
                            booklet_number=booklet_number,
                            defaults={'signin_flag': signin_flag, 'signout_flag': signout_flag, 'biometric_data': biometry, 'exam_attendace': exam_attend_id_value}
                        )
                        if not created:
                            # If the record already exists, update the signout_flag
                            attendance.signout_flag = signout_flag
                            attendance.save()
                        success = {'success': True}
                        return JsonResponse(success, safe=False)                        
                    else:
                        return JsonResponse({'success': False, 'error_message': 'Exam attendance not found.'}, safe=False)
            else:
                return JsonResponse({'success': False, 'error_message': 'Fingerprint does not match.'}, safe=False)
        else:
            return JsonResponse({'success': False, 'error_message': 'Form is not valid.'}, safe=False)
        
    # get student who attend exam
    elif request.method == "GET" and 'get_programme_to_student' in request.GET:
        programme_id = request.GET['get_programme_to_student']
        programme_to_take = Exam_attendace.objects.filter(programme_id=programme_id).first()
        student_historys = list(Final_exam_attendence_record.objects.order_by('-id').filter(exam_attendace=programme_to_take.id))
        serialized_data = serialize('json', student_historys)
        return JsonResponse(serialized_data, safe=False)

    # else:
    form = Exam_attendace_form()
    programme_ids = Programme.objects.filter(id__in=Exam_attendace.objects.filter(exam_status='on progress').values_list('programme_id', flat=True)).distinct()
    context = {
        'form': form,
        'examData': Exam_attendace.objects.all(),
        'units': Unit.objects.all(),
        'semesters': Semester.objects.all(),
        'exam_records': Exam_attendace.objects.order_by('-created_at'),
        'programme_ids': programme_ids,
    }
    template = "exam/exam_attendance.html"
    return render(request, template, context)


# edit student info and update biometric data
def edit_student_info(request, id):
    user_student = get_object_or_404(Student, id=id)
    if request.method == "GET":
        context = {'form': StudentForm(instance=user_student), 'id':id}
        tamplete = "user/edit_student_info.html"
        return render(request, tamplete, context)
    elif request.method == "POST":
        user_student_form = StudentForm(request.POST, instance=user_student)
        if user_student_form.is_valid():
           user_student_form.save()
        return JsonResponse({'success': True}, safe=False)
    

# update biometric data
def edit_and_add_student_fingerprint(request, id):
    user_student = get_object_or_404(Student, id=id)
    if request.method == "GET":
        finger_data = Biometric_data.objects.filter(student=id)
        context = {
            'finger': finger_data
        }
        tamplete = "user/edit_and_add_student_fingerprint.html"
        return render(request, tamplete, context)
    elif request.method == "POST":
        fingerprint = request.POST.get('fingerprint')
        # biometric_data_form = Biometric_data_form({ 'fingerprint': fingerprint, 'student': user_student.id })
        biometric_data_form = Biometric_data_form({ 'fingerprint': fingerprint, 'student': user_student.id })
        if biometric_data_form.is_valid():
            biometric_data_form.save()
        else:
            return JsonResponse({'success': False}, safe=False)
        return JsonResponse({'success': True}, safe=False)
    

# exam_attendance_step_two
def exam_attendance_step_two(request):
    programme_ids = Programme.objects.filter(
        exam_attendace__exam_status='on progress'
    ).values('name', 'id').distinct()
    
    # programme_ids = Programme.objects.all()
    # student_who_can_attend
    if request.method == "GET" and 'programme_id' in request.GET:
        programme_id = request.GET['programme_id']

        # Filter students who have signed in but not signed out yet for the selected programme
        students_signed_in_not_signed_out = Student.objects.filter(
            biometric_data__final_exam_attendence_record__signout_flag=0,
            programme_id=programme_id
        ).distinct()

        # Filter students who have not signed in yet for the selected programme
        students_not_signed_in_yet = list(Student.objects.filter(programme_id=programme_id))

        # Serialize the queryset to dictionaries
        signed_in_not_signed_out_data = [{'reg_number': student.reg_number} for student in students_signed_in_not_signed_out]
        not_signed_in_yet_data = [{'reg_number': student.reg_number} for student in students_not_signed_in_yet]

        # Return JSON response with both lists
        return JsonResponse({
            'signed_in_not_signed_out': signed_in_not_signed_out_data,
            'not_signed_in_yet': not_signed_in_yet_data
        })
    
    context = {
        'programme_ids': programme_ids,
        'template': 'exam/exam_attendance_step_two.html',
    }
    return render(request, context['template'], context)

# submit_signin_student
def submit_signin_student(request):
    if request.method == 'POST':          
        booklet_number = request.POST.get('booklet_number')
        reg_number = request.POST.get('reg_number')
        biometric_data = request.POST.get('biometric_data')
        
        try:
            student = Student.objects.get(reg_number=reg_number)
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Student not found.'}, safe=False)
        
        fingerprint_match_exists = Biometric_data.objects.get(fingerprint=biometric_data)
        if fingerprint_match_exists:
            student = Student.objects.get(reg_number=reg_number)
            student_programme = student.programme_id
            if student_programme is not None:
                programme_id_value = student_programme
                exam_attend = Exam_attendace.objects.filter(programme_id=programme_id_value).first()
                if exam_attend is not None:
                    exam_attend_id_value = exam_attend
                    biometry = fingerprint_match_exists
                    attendance, created = Final_exam_attendence_record.objects.get_or_create(
                        booklet_number=booklet_number,
                        defaults={'signout_flag': False, 'signin_flag': True, 'biometric_data': biometry, 'exam_attendace': exam_attend_id_value}
                    )
                    attendance.save()
                    success = {'success': True}
                    return JsonResponse(success, safe=False)                        
                else:
                    return JsonResponse({'success': False, 'error_message': 'Exam attendance not found.'}, safe=False)
        else:
            return JsonResponse({'success': False, 'error_message': 'Fingerprint does not match.'}, safe=False)
        
# submit_signout_student
def submit_signout_student(request):
    if request.method == 'POST':
        reg_number = request.POST.get('reg_number')
        biometric_data = request.POST.get('biometric_data')        
        
        try:
            student = Student.objects.get(reg_number=reg_number)
        except Student.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Student not found.'}, safe=False)
        
        try:
            fingerprint_match = Biometric_data.objects.get(fingerprint=biometric_data)
        except Biometric_data.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Biometric data not found.'}, status=400)
        
        if fingerprint_match.student != student:
            return JsonResponse({'success': False, 'error_message': 'Biometric data does not match the student.'}, status=400)
        
        exam_attendance = Exam_attendace.objects.filter(programme_id=student.programme_id).first()
        if not exam_attendance:
            return JsonResponse({'success': False, 'error_message': 'Exam attendance not found for student.'}, status=400)
        
        final_attendance_record = Final_exam_attendence_record.objects.filter(
            biometric_data=fingerprint_match,
            exam_attendace=exam_attendance,
            signout_flag=False
        ).first()

        if not final_attendance_record:
            return JsonResponse({'success': False, 'error_message': 'No active attendance record found.'}, status=400)
                
        final_attendance_record.signout_flag = True
        final_attendance_record.save()
                
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error_message': 'Invalid request method.'}, status=400)

# logout
# def logout(request):
#     auth.logout(request)
#     return render('authentication/logout.html')
