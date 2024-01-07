from django.urls import path
from . import views
from .views import student_cw
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("forgot_password", views.forgot_password, name="forgot_password"),
    path("footer", views.footer, name="footer"),
    path("home", views.home, name="home"),
    path("layout", views.layout, name="layout"),
    path("footer1", views.footer1, name="footer1"),
    path("student", views.student, name="student"),
    path("staff", views.staff, name="staff"),
    # user profile
    path("profile", views.profile, name="profile"),
    path("staff_profile", views.profile, name="staff_profile"),
    path("student_profile", views.profile, name="student_profile"),
    path("depertment", views.depertment, name="depertment"),
    path("unit", views.unit, name="unit"),
    path("year_of_study", views.year_of_study, name="year_of_study"),
    path("programme", views.programme, name="programme"),
    path("education_level", views.education_level, name="education_level"),
    path("semester", views.semester, name="semester"),
    path("course", views.course, name="course"),

    # student_semester_registration
    path("student_semester_registration", views.student_semester_registration, name="student_semester_registration"),
    # programme_stracture
    path("programme_stracture", views.programme_stracture, name="programme_stracture"),
    # register_my_course
    path("register_my_course", views.register_my_course, name="register_my_course"),

    # exam_attendance, payment
    path("exam_attendance", views.exam_attendance, name="exam_attendance"),
    path("payment", views.payment, name="payment"),
    # path("student_cw", views.student_cw, name="student_cw")
    path('student_cw/', student_cw, name='student_cw'),
    # edit student info and update biometric data
    path('edit_student_info/<int:id>/', views.edit_student_info, name="edit_student_info"),
    path('edit_and_add_student_fingerprint/<int:id>/', views.edit_and_add_student_fingerprint, name="edit_and_add_student_fingerprint")
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
