from django.contrib import admin
from .models import Prompt, Scores, Story

admin.site.register(Story)
admin.site.register(Prompt)
admin.site.register(Scores)

# Register your models here.
