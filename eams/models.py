from datetime import timezone
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Unit(models.Model):
    name = models.CharField(max_length=200)
    unit_abbreviation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def ___str__(self):
        return self.unit_abbreviation
    class Meta:
        db_table = "unit"
    # END OF UNITS MODEL

class Department(models.Model):
    name = models.CharField(max_length=200)
    department_abbreviation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    def __str__(self):
        return self.department_abbreviation
    class Meta:
        db_table = "department"
    # END OF DEPERMENT MODEL


class Year_of_study(models.Model):
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def ___str__(self):
        return self.year
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
    def ___str__(self):
        return self.programme_abbrevation
        # return f"{self.name} {self.programme_abbrevation}"
    class Meta:
        db_table = "programme"
    # END OF PROGRAMME MODEL

class Education_level(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "education_level"
    # END OF EDUCATION_LEVEL MODEL

class Semester(models.Model):
    CHOICE_NAME = (
        ('1', 'one'),
        ('2', 'two')
    )
    name = models.CharField(max_length=200, choices=CHOICE_NAME, default=1)
    semester_start_at = models.DateField()
    semester_end_at = models.DateField()
    status = models.TextField(default='continuing')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "semester"
    # END OF SEMESTER MODEL

class Course(models.Model):
    CHOICE_TYPE = (
        ('Core', 'Core'),
        ('None Core', 'None Core')
    )
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=CHOICE_TYPE, default='Core')
    credit = models.FloatField(default=8.00)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "course"
    # END OF COURSE MODEL

class Course_programme(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        db_table = "course_programme"
    # END OF Course_programme MODEL


# user
class CustomStudentUser(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email Field Is Required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_staff=True.")        
        return self.create_user(email, password, **extra_fields)

# class Student(AbstractBaseUser, PermissionsMixin):
class Student(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    def default_depertment():
        try:
            return Department.objects.get(pk=1)
        except Department.DoesNotExit:
            return None
    def default_programme():
        try:
            return Programme.objects.get(pk=1)
        except Programme.DoesNotExit:
            return None
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    middle_name = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True)
    cell_phone = models.CharField(max_length=20, null=True)
    reg_number = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='male')
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, default=default_programme)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = "student"
    def __str__(self):
        # return f"{self.reg_number}"
        return self.reg_number
    
class Staff(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    def default_depertment():
        try:
            return Department.objects.get(pk=1)
        except Department.DoesNotExit:
            return None
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    middle_name = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True)
    cell_phone = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='male')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=default_depertment)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        db_table = "staff"
    def __str__(self):
        return self.email

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    receipt = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.amount
    class Meta:
        db_table = "payment"
    # END OF Payment MODEL

class Biometric_data(models.Model):
    fingerprint = models.CharField(max_length=500)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table ="exam_attendace"

    def __str__(self):
        return f"{self.user.username}'s {self.get_type_of_exam_display()} Exam Attendance"    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()
    class Meta:
        db_table = 'profile'
    def __str__(self):
        if self.user:
            return self.user.username
        elif self.student:
            return self.student.username 
        else:
            return "Not Student User Or Staff"


# student_semester_registration
class SemesterRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    semester_registration_status = models.CharField(max_length=100, default='registered')
    # semester_end_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'SemesterRegistration'
    def __str__(self):
        return self.semester_registration_status