from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import PersonInfo


class MainPageView(View):
    def get(self, request):
        person_info = PersonInfo.objects.all()
        data = {

        }
        return render(request, "main_page.html", data)

