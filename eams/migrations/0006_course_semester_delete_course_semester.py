# Generated by Django 4.2.5 on 2023-09-20 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eams', '0005_alter_biometric_data_table_alter_course_table_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eams.semester'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Course_semester',
        ),
    ]