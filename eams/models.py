from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    department_abbreviation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "department"
    def __str__(self):
        return self.name
    # END OF DEPERMENT MODEL

class Unit(models.Model):
    name = models.CharField(max_length=200)
    unit_abbreviation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = "unit"
    # END OF UNITS MODEL


class Year_of_study(models.Model):
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "year_of_study"
    # END OF Year_of_study MODEL


class Programme(models.Model):
    name = models.CharField(max_length=200)
    programme_abbrevation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year_of_study = models.ForeignKey(Year_of_study, on_delete=models.CASCADE)

    class Meta:
        db_table = "programme"
    # END OF PROGRAMME MODEL


class Education_level(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "education_level"
    # END OF EDUCATION_LEVEL MODEL


class Semester(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "semester"
    # END OF SEMESTER MODEL


class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "course"
    # END OF COURSE MODEL


class Course_programme(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "course_programme"
    # END OF Course_programme MODEL


class Payment(models.Model):
    amount = models.IntegerField()
    status = models.BooleanField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "payment"
    # END OF Payment MODEL


class Biometric_data(models.Model):
    fingerprint = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = "biometric_data"
    # END OF Biometric_data MODEL


class Exam_attendace(models.Model):
    EXAM_TYPES = (
        ('ue', 'University Exam'),
        ('se', 'Supplementary Exam'),
        ('t1', 'Test One'),
        ('t2', 'Test Two'),
    )
    type_of_exam = models.CharField(max_length=2, choices=EXAM_TYPES, default='ue')
    booklet_number = models.CharField(max_length=100)
    exam_start_time = models.TimeField
    exam_end_time = models.TimeField
    signin_fingerprint = models.BinaryField()
    signout_fingerprint = models.BinaryField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table ="exam_attendace"

    def __str__(self):
        return f"{self.user.username}'s {self.get_type_of_exam_display()} Exam Attendance"

