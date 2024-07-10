# Generated by Django 5.0.6 on 2024-07-08 12:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('timetable', models.JSONField()),
                ('room_allocation', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_info', models.JSONField()),
                ('academic_info', models.JSONField()),
                ('disciplinary_info', models.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=5)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_information.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('withdrawal_date', models.DateField(blank=True, null=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_information.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')], max_length=7)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_information.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_information.student')),
            ],
        ),
    ]
