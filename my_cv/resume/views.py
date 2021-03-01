from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from .models import PersonInfo, Skill
from .forms import ContactMeForm


class MainPageView(View):
    def get(self, request):
        personal_info = PersonInfo.objects.all()[0]
        print(personal_info)
        print(Skill.objects.all())

        skills = Skill.objects.all()

        data = {
            "personal_info": personal_info,
            "skills": skills,
        }

        return render(request, "main_page.html", data)

class ContactMeView(View):
    def get(self, request):
        form = ContactMeForm()
        return render(request, "contact_me/contact_me.html", {"form": form})

    def post(self, request):
        # todo добавить тг бота який буде адміну кидати сповіщення
        form = ContactMeForm(request.POST)
        error = ""
        if form.is_valid():
            form.save()
            return redirect('home_page')
        else:
            error = "form is not valid"

        data = {
            "form": form,
            "error": error,
        }

        return render(request, "contact_me/contact_me.html", data)