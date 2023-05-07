from django.urls import path 
from . import views
urlpatterns = [
    path('getstarted',views.getstarted,name="getstarted"),
    path('Register',views.registerprof,name="registerprof"),
    path('Dashboard',views.dashboardprof,name="dashboardprof"),
    path('Dashboard/courses',views.dashboardcourses,name="dashboardcourses"),
    path('Dashboard/createcourse',views.createcourse,name="createcourse"),


]
