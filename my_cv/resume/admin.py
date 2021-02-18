from django.contrib import admin

# Register your models here.
from .models import PersonInfo, Skill, Experience, Study

admin.site.register(PersonInfo)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Study)
