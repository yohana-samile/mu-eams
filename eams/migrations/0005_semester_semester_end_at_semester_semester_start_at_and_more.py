# Generated by Django 4.2.5 on 2023-11-22 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eams', '0004_semesterregistration_delete_semesterregistrationform'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='semester_end_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='semester_start_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='status',
            field=models.TextField(default='continuing'),
        ),
    ]