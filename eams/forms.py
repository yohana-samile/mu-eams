from django import forms
from .models import Department, Unit, Year_of_study, Programme, Education_level, Semester, Course


# Department
class FormDepertment(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'department_abbreviation']

# unit
class FormUnit(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', 'unit_abbreviation', 'department']

#year
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