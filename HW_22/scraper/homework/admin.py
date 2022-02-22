from django.contrib import admin
from .models import Newstories, Showstories, Jobstories, Askstories

admin.site.register(Askstories)

admin.site.register(Newstories)

admin.site.register(Showstories)

admin.site.register(Jobstories)
