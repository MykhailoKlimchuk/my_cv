from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from .models import PersonInfo


class MainPageView(View):
    def get(self, request):
        personal_info = PersonInfo.objects.all()[0]
        data = {
            "ggg": "11",
            "personal_info": personal_info
        }
        return render(request, "main_page.html", data)

