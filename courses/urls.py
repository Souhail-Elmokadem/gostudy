from django.urls import path 
from . import views
urlpatterns = [
    path('',views.CoursesList,name='CoursesList'),
    path('course/<int:pk>',views.coursedetails,name='coursedetails')

]
