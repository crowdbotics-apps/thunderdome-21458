from django.contrib import admin
from .models import Prompt, Story

admin.site.register(Story)
admin.site.register(Prompt)

# Register your models here.
