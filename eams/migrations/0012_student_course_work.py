# Generated by Django 3.2.12 on 2023-12-22 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eams', '0011_remove_staff_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_course_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_work', models.FloatField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eams.course')),
                ('programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eams.programme')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eams.staff')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eams.student')),
            ],
            options={
                'db_table': 'student_course_work',
            },
        ),
    ]
