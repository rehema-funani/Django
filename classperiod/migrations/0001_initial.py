# Generated by Django 5.0.7 on 2024-07-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('course', models.CharField(max_length=40)),
                ('classroom', models.CharField(max_length=40)),
                ('day_of_the_week', models.CharField(max_length=40)),
            ],
        ),
    ]
