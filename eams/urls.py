from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("forgot_password", views.forgot_password, name="forgot_password"),
    path("footer", views.footer, name="footer"),
    path("home", views.home, name="home"),
    path("layout", views.layout, name="layout"),
    path("footer1", views.footer1, name="footer1"),
    path("student", views.student, name="student"),
    path("staff", views.staff, name="staff"),
    path("depertment", views.depertment, name="depertment"),
    path("unit", views.unit, name="unit"),
    path("year_of_study", views.year_of_study, name="year_of_study"),
    path("programme", views.programme, name="programme"),
    path("education_level", views.education_level, name="education_level"),
    path("semester", views.semester, name="semester"),
    path("course", views.course, name="course"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
