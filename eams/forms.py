from django import forms
from django.contrib.auth.models import User
from .models import Unit, Department, Year_of_study, Programme, Education_level, Semester, Course, Student, SemesterRegistration, Payment, Staff, Exam_attendace
class FormUnit(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'unit_abbreviation']

# Department
class FormDepertment(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'department_abbreviation', 'unit']

# Year
class FormYearOFStudy(forms.ModelForm):
    class Meta:
        model = Year_of_study
        fields = ['year']

# FormProgramme
class FormProgramme(forms.ModelForm):
    class Meta:
        model = Programme
        fields = ['name', 'programme_abbrevation', 'department', 'year_of_study']

# FormEducationLevel
class FormEducationLevel(forms.ModelForm):
    class Meta:
        model = Education_level
        fields = ['name']

# semester
class FormSemester(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name', 'semester_start_at', 'semester_end_at']
        widgets = {
            'semester_start_at': forms.DateInput(attrs={'type': 'date'}),
            'semester_end_at': forms.DateInput(attrs={'type': 'date'}),
        }

# FormCourse
class FormCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'semester', 'type', 'credit']

# student 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']

# StaffForm
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['user']

# student_semester_registration
class SemesterRegistrationForm(forms.ModelForm):
    class Meta:
        model = SemesterRegistration
        fields = ['semester']

# student payment
class Payment_for_Student(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'student']


# exam attendence
class Exam_attendace(forms.ModelForm):
    class Meta:
        model = Exam_attendace
        fields = ['type_of_exam', 'exam_start_time', 'exam_end_time', 'booklet_number', 'biometric_data', 'programme', 'course']
        widgets = {
            'exam_start_time': forms.DateInput(attrs={'type': 'date'}),
            'exam_end_time': forms.DateInput(attrs={'type': 'date'}),
        }