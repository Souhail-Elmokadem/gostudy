from django.urls import path 
from . import views
urlpatterns = [
    path('getstarted',views.getstarted,name="getstarted"),
    path('Register',views.registerprof,name="registerprof"),
    path('Dashboard',views.dashboardprof,name="dashboardprof"),
    path('Dashboard/courses',views.dashboardcourses,name="dashboardcourses"),
    path('Dashboard/createcourse',views.createcourse,name="createcourse"),
    path('Dashboard/editcourse/<int:pk>',views.editcourse,name="editcourse"),
    path('delete/<int:pk>',views.deletecourse,name='deletecourse'),
    path('addroleprof/<int:pk>',views.addroleprof,name='addroleprof'),
    path('logout',views.userlogout,name='logoutprof')
]
