# Generated by Django 3.2.12 on 2023-12-31 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eams', '0018_auto_20231229_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_attendace',
            name='biometric_data',
        ),
        migrations.RemoveField(
            model_name='exam_attendace',
            name='booklet_number',
        ),
        migrations.RemoveField(
            model_name='exam_attendace',
            name='signin_fingerprint',
        ),
        migrations.RemoveField(
            model_name='exam_attendace',
            name='signout_fingerprint',
        ),
        migrations.CreateModel(
            name='Final_exam_attendence_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booklet_number', models.CharField(max_length=100)),
                ('signin_flag', models.BinaryField()),
                ('signout_flag', models.BinaryField(null=True)),
                ('biometric_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eams.biometric_data')),
                ('exam_attendace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eams.exam_attendace')),
            ],
            options={
                'db_table': 'final_exam_attendence_record',
            },
        ),
    ]
