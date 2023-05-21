from django.urls import path
from . import views
urlpatterns = [
    path('login',views.etudiant_login,name='etudiant_login'),
    path('register',views.etudiant_register,name='etudiant_register'),
    path('profile',views.profile,name='profile'),
    path('update/profile',views.updateProfile,name='updateprofile'),
    path('update/Password',views.PasswordChangeView.as_view(template_name = "etudiant/updatePassword.html"),name='updatePassword'),
]
