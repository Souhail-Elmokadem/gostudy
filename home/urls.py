from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('ai',views.ai,name='ai'),
]

