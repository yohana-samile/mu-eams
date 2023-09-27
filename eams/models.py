from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

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
        return f"{self.name} {self.programme_abbrevation}"

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
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "semester"
    # END OF SEMESTER MODEL

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
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

class Payment(models.Model):
    amount = models.IntegerField()
    status = models.BooleanField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.amount

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
            
# class Student(models.Model):
class Student(AbstractBaseUser):
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
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    birth_date = models.DateField(null=True)
    cell_phone = models.CharField(max_length=20, null=True)
    reg_number = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='male')
    # department = models.ForeignKey(Department, on_delete=models.CASCADE, default=default_depertment)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, default=default_programme)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/', null=True)
    date_joined = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    USERNAME_FIELD = 'reg_number'
    class Meta:
        db_table = "student"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"