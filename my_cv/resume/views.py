from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import PersonInfo, Skill


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

