# Generated by Django 3.2.12 on 2023-12-22 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eams', '0012_student_course_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_course_work',
            old_name='course_work',
            new_name='course_work_value',
        ),
    ]
