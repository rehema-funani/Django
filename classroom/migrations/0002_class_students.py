# Generated by Django 5.0.7 on 2024-08-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
        ('student', '0003_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='student.student'),
        ),
    ]
