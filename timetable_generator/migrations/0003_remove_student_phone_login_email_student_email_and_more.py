# Generated by Django 5.1.2 on 2024-10-26 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable_generator', '0002_login_student_login_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='abc@gmail.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.BigIntegerField(default=1, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='login',
            name='role',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='login_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timetable_generator.login'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=254, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('department', models.CharField(max_length=40)),
                ('mobile', models.BigIntegerField(default=1)),
                ('login_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timetable_generator.login')),
            ],
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=254, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('department', models.CharField(max_length=40)),
                ('mobile', models.BigIntegerField(default=1)),
                ('login_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='timetable_generator.login')),
            ],
        ),
    ]
