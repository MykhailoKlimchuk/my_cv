from django.db import models
from django.core.validators import RegexValidator


class PersonInfo(models.Model):
    full_name = models.CharField("Ім'я", max_length=200)
    birthday = models.DateField("День народження")
    main_image = models.ImageField("Головне фото", upload_to="resume_main_photo/")
    about_me = models.TextField("Про мене")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField("Телефон", validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField("Пошта")
    github = models.CharField("github", max_length=200)
    linkedin = models.CharField("linkedin", max_length=200)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Інформація про людину"
        verbose_name_plural = "Інформація про людей"


class Skill(models.Model):
    person_info = models.ForeignKey(PersonInfo, verbose_name="Інформація про людину", on_delete=models.CASCADE)
    skill_name = models.CharField("Назва скіла", max_length=200)


class Experience(models.Model):
    person_info = models.ForeignKey(PersonInfo, verbose_name="Інформація про людину", on_delete=models.CASCADE)
    company_name = models.CharField("Назва компанії", max_length=200)
    position = models.CharField("Посада", max_length=200)
    description_of_responsibilities = models.TextField("Опис обовязків")
    start_work_date = models.DateField("Початок роботи")
    finish_work_date = models.DateField("Кінець роботи")


class Study(models.Model):
    person_info = models.ForeignKey(PersonInfo, verbose_name="Інформація про людину", on_delete=models.CASCADE)
    study_place_name = models.CharField("Назва місця навчання", max_length=200)
    specialty_name = models.CharField("Спеціальність", max_length=200)
    finish_level = models.CharField("Рівень після закінчення", max_length=200)
    start_study_date = models.DateField("Початок навчання")
    finish_study_date = models.DateField("Кінець навчання")


class Contact(models.Model):
    pass


