# Generated by Django 5.1.2 on 2024-11-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable_generator', '0003_remove_student_phone_login_email_student_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depname', models.CharField(max_length=40)),
                ('dept_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
