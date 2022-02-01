from .views import index, askstories, showstories, jobstories, newstories
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('askstories/', askstories, name='askstories'),
    path('showstories/', showstories, name='showstories'),
    path('jobstories/', jobstories, name='jobstories'),
    path('newstories/', newstories, name='newstories')
]
