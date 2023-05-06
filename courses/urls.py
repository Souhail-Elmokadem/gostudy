from django.urls import path 
from . import views
urlpatterns = [
    path('',views.CoursesList,name='CoursesList'),
    path('<int:pk>',views.CoursesListS,name='CoursesListS'),
    path('course/<int:pk>',views.coursedetails,name='coursedetails'),
    path('Enroll/<int:pk>',views.EnrollCourse,name='EnrollCourse'),
    path('course/view/<int:pk>',views.viewCourse,name='ViewCourse'),

]
