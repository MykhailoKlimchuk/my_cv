# Generated by Django 3.1.6 on 2021-02-18 07:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name="Ім'я")),
                ('birthday', models.DateField(verbose_name='День народження')),
                ('main_image', models.ImageField(upload_to='resume_main_photo/', verbose_name='Головне фото')),
                ('about_me', models.TextField(verbose_name='Про мене')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Пошта')),
                ('github', models.CharField(max_length=200, verbose_name='github')),
                ('linkedin', models.CharField(max_length=200, verbose_name='linkedin')),
            ],
            options={
                'verbose_name': 'Інформація про людину',
                'verbose_name_plural': 'Інформація про людей',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_place_name', models.CharField(max_length=200, verbose_name='Назва місця навчання')),
                ('specialty_name', models.CharField(max_length=200, verbose_name='Спеціальність')),
                ('finish_level', models.CharField(max_length=200, verbose_name='Рівень після закінчення')),
                ('start_study_date', models.DateField(verbose_name='Початок навчання')),
                ('finish_study_date', models.DateField(verbose_name='Кінець навчання')),
                ('person_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.personinfo', verbose_name='Інформація про людину')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200, verbose_name='Назва скіла')),
                ('person_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.personinfo', verbose_name='Інформація про людину')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, verbose_name='Назва компанії')),
                ('position', models.CharField(max_length=200, verbose_name='Посада')),
                ('description_of_responsibilities', models.TextField(verbose_name='Опис обовязків')),
                ('start_work_date', models.DateField(verbose_name='Початок роботи')),
                ('finish_work_date', models.DateField(verbose_name='Кінець роботи')),
                ('person_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.personinfo', verbose_name='Інформація про людину')),
            ],
        ),
    ]