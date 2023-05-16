from django.urls import path
from . import views
urlpatterns = [
    path('login',views.etudiant_login,name='etudiant_login'),
    path('register',views.etudiant_register,name='etudiant_register'),
    path('profile',views.profile,name='profile')
]
