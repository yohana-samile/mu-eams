# Generated by Django 3.2.12 on 2023-12-29 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eams', '0017_exam_attendace'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_attendace',
            name='exam_end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam_attendace',
            name='exam_start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
