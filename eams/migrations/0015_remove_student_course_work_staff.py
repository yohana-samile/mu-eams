# Generated by Django 3.2.12 on 2023-12-22 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eams', '0014_alter_student_course_work_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_course_work',
            name='staff',
        ),
    ]
