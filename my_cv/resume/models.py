from django.db import models



class PersonInfo(models.Model):
    full_name = models.CharField("Ім'я", max_length=200)
    birthday = models.DateField("День народження")
    main_image = models.ImageField("Головне фото", upload_to="resume_main_photo/")
    about_me = models.TextField("Про мене")

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
