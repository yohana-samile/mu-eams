from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from eams.models import Student, Staff

class UserStudentAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        try:
            student = Student.objects.get(reg_number=username)
        except Student.DoesNotExist:
            student = None
        
        try:
            staff = Staff.objects.get(rol_number=username)
        except Staff.DoesNotExist:
            staff = None

        if user is not None and user.check_password(password):
            return user
        elif student is not None and student.check_password(password):
            return student
        elif staff is not None and staff.check_password(password):
            return staff
        else:
            return None
        
