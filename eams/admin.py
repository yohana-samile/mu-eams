from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as OrigUserAdmin
admin.site.unregister(get_user_model())
from .models import Unit, Department, Programme, Student, Staff, Course, Semester, Education_level, Year_of_study

# Register your models here.

User = get_user_model()

@admin.register(User)
class UserAdmin(OrigUserAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'username', 'email', 'is_active'
    )

admin.site.register(Unit)
admin.site.register(Department)
admin.site.register(Programme)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Education_level)
admin.site.register(Year_of_study)