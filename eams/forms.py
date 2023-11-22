from django import forms
from django.contrib.auth.models import User
from .models import Unit, Department, Year_of_study, Programme, Education_level, Semester, Course, Student, SemesterRegistrationForm
from django.contrib.auth.forms import UserCreationForm
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
        fields = ['name']

# FormCourse
class FormCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'semester']

# student 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']
        # fields = ['email', 'password', 'first_name', 'last_name', 'middle_name', 'birth_date', 'cell_phone', 'reg_number', 'gender', 'programme']

# student_semester_registration
class SemesterRegistrationForm(forms.ModelForm):
    class Meta:
        model = SemesterRegistrationForm
        fields = ['semester']
